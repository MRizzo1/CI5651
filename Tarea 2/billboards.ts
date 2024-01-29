interface BillboardR {
  p: number;
  t: number;
}

// We want to select the one with shortest finishing point that does not conflict with the ones already selected
function selectRequest(request: BillboardR, lastEndPoint: number) {
  return request.p >= lastEndPoint;
}

function maximalRequests(requests: Array<BillboardR>) {
  // Sorting by the end points of the billboard
  const sortedRequests = [...requests].sort(
    (b1: BillboardR, b2: BillboardR) => b1.p + b1.t - (b2.p + b2.t)
  );
  let maximalSet: Array<BillboardR> = [];
  let lastEndPoint: number = -1;

  sortedRequests.forEach((request) => {
    if (selectRequest(request, lastEndPoint)) {
      maximalSet.push(request);
      lastEndPoint = request.p + request.t;
    }
  });

  return maximalSet;
}

const test: Array<BillboardR> = [
  { p: 1, t: 4 },
  { p: 2, t: 1 },
  { p: 3, t: 3 },
];
console.log(maximalRequests(test));
