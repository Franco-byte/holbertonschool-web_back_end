export default function appendToEachArrayValue(array, appendString) {
  const copy = [...array];
  let idx = 0;
  for (const value of array) {
    copy[idx] = appendString + value;
    idx += 1;
  }

  return copy;
}
