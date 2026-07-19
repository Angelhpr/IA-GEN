import { apiFetch } from "../lib/api";

export interface ChatRequest {
  message: string;
}

export interface ChatResponse {
  response: string;
}

export async function sendMessage(question: string): Promise<string> {
  const data = await apiFetch<ChatResponse>("/api/chat", {
    method: "POST",
    body: JSON.stringify({
      message: question,
    } satisfies ChatRequest),
  });

  return data.response;
}
