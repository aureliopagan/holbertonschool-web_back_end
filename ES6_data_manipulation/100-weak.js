export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  // Get current count for this endpoint, default to 0 if not found
  let count = weakMap.get(endpoint) || 0;
  
  // Increment the count
  count += 1;
  
  // Update the count in the WeakMap
  weakMap.set(endpoint, count);
  
  // Check if the count has reached the limit
  if (count >= 5) {
    throw new Error('Endpoint load is high');
  }
}