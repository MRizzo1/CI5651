interface NodeInterface {
  data: number;
  heapPriority: number;
  count: number;
  rev: boolean;
  left: NodeInterface | null;
  right: NodeInterface | null;
}

function getRandom(max: number, min: number = 1) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}

function getCount(n: NodeInterface | null) {
  return !!n ? n.count : 0;
}

function updateCount(n: NodeInterface | null) {
  if (!n) return;
  n.count = getCount(n.left) + getCount(n.right) + 1;
}

function multiswapTreap(n: NodeInterface | null) {
  if (!n) return;

  if (n.rev) {
    n.rev = false;
    [n.left, n.right] = [n.right, n.left];

    if (!!n.left) n.left.rev = true;
    if (!!n.right) n.right.rev = true;
  }
}

function mergeTreap(
  left: NodeInterface | null,
  right: NodeInterface | null) {

  multiswapTreap(left);
  multiswapTreap(right);
  if (!left || !right) {
    return !!left ? left : right;
  }

  if (left.heapPriority > right.heapPriority) {
    left.right = mergeTreap(left.right, right);
    updateCount(left);
    return left;
  }

  right.left = mergeTreap(left, right.left);
  updateCount(right);
  return right;
}

function splitTreap(key: number, n: NodeInterface | null) {
  if (!n) return [null, null];
  multiswapTreap(n);

  let implKey = 1 + getCount(n.left);
  let result: Array<NodeInterface | null>;

  if (key < implKey) {
    result = splitTreap(key, n.left);
    n.left = result[1];
    updateCount(n);
    return [result[0], n];
  } else {
    result = splitTreap(key - implKey, n.right);
    n.right = result[0];
    updateCount(n);
    return [n, result[1]];
  }
}

function reverseTreap(l: number, r: number, root: NodeInterface | null) {
  let result1: Array<NodeInterface | null>;
  let result2: Array<NodeInterface | null>;
  result1 = splitTreap(l, root);
  result2 = splitTreap(r - l + 1, result1[1]);

  result2[0] ? (result2[0].rev = true) : null;
  return mergeTreap(mergeTreap(result1[0], result2[0]), result2[1]);
}

function initializeNode(data: number) {
  let n: NodeInterface = {
    data: data,
    count: 1,
    heapPriority: getRandom(100),
    rev: false,
    left: null,
    right: null,
  };
  return n;
}

function insertTreap(key: number, data: number, root: NodeInterface | null) {
  let n: NodeInterface = initializeNode(data);
  let treaps: Array<NodeInterface | null> = splitTreap(key, root);
  return mergeTreap(mergeTreap(treaps[0], n), treaps[1]);
}

function arrayPrint(root: NodeInterface | null) {
  if (!root || !root.data) return;
  arrayPrint(root.left);
  console.log(root.data);
  arrayPrint(root.right);
}

let root: NodeInterface | null = null;
let reversed: NodeInterface | null = null;
root = insertTreap(0, 1, root);
root = insertTreap(1, 2, root);
root = insertTreap(2, 3, root);
root = insertTreap(3, 4, root);
root = insertTreap(4, 5, root);
root = insertTreap(5, 6, root);

arrayPrint(root);
console.log("----------------");
reversed = reverseTreap(0, 1, root);
console.log("REVERSED");
arrayPrint(reversed);
reversed = reverseTreap(1, 5, reversed);
console.log("REVERSED");
arrayPrint(reversed);
