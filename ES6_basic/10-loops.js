export default function appendToEachArrayValue(array, appendString) {
  const copy = [...array];
  for (const [idx, value] of array.entries()) {
    copy[idx] = appendString + value;
  }

  return copy;
}
