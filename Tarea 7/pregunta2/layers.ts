interface Point {
    x: number;
    y: number;
  }
  
  function crossProduct(origin: Point, pointA: Point, pointB: Point) {
    return (
      (pointA.x - origin.x) * (pointB.y - origin.y) -
      (pointA.y - origin.y) * (pointB.x - origin.x)
    );
  }
  
  function convexHull(points: Array<Point>) {
    let n: number = points.length;
    let lowerHull: Array<Point> = [];
    let upperHull: Array<Point> = [];
  
    if (n <= 1) return points;
  
    points.sort((a: Point, b: Point) => {
      return a.x == b.x ? a.y - b.y : a.x - b.x;
    });
  
    for (let i = 0; i < n; i++) {
      let p = points[i];
      while (
        lowerHull.length >= 2 &&
        crossProduct(
          lowerHull[lowerHull.length - 2],
          lowerHull[lowerHull.length - 1],
          p
        ) <= 0
      ) {
        lowerHull.pop();
      }
      lowerHull.push(p);
    }
  
    for (let i = n - 1; i >= 0; i--) {
      let p = points[i];
      while (
        upperHull.length >= 2 &&
        crossProduct(
          upperHull[upperHull.length - 2],
          upperHull[upperHull.length - 1],
          p
        ) <= 0
      ) {
        upperHull.pop();
      }
      upperHull.push(p);
    }
  
    return [...lowerHull.slice(0, -1), ...upperHull.slice(0, -1)];
  }
  
  
  function convexLayers(points: Array<Point>){
  
      let layers: Array<Array<Point>> = []
      let hull: Array<Point>  
  
      while (points.length > 0){
          hull = convexHull(points);
  
          points = points.filter(p => !(new Set(hull).has(p)));
  
          layers.push(hull)
      }
      
      return layers;
  }
  