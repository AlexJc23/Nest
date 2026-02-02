const API_URL = process.env.EXPO_PUBLIC_API_URL;;

export async function apiGet(path: string) {
  const response = await fetch(`${API_URL}${path}`);
  if (!response.ok) {
    throw new Error(`API request failed with status ${response.status}`);
  }
    return response.json();
    }
