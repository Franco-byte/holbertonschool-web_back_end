export default function appendToEachArrayValue(array, appendString) {
  for (const [idx, value] of array) {
    const copy = array;
    copy[idx] = appendString + value;
  }

  return array;
}
