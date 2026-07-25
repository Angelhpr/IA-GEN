import { apiFetch } from "../lib/api";
import type { Message } from "../types/message";

const MAX_HISTORY_CONTENT_LENGTH = 5000;

export type ChatHistoryMessage = Pick<Message, "role" | "content">;

export interface ChatRequest {
  message: string;
  history: ChatHistoryMessage[];
}

export interface ChatResponse {
  response: string;
}

export async function sendMessage(
  question: string,
  history: ChatHistoryMessage[] = []
): Promise<string> {
  const normalizedHistory: ChatHistoryMessage[] = history.map(
    ({ role, content }) => ({
      role,
      content: content.slice(0, MAX_HISTORY_CONTENT_LENGTH),
    })
  );

  const data = await apiFetch<ChatResponse>("/api/chat", {
    method: "POST",
    body: JSON.stringify({
      message: question,
      history: normalizedHistory,
    } satisfies ChatRequest),
  });

  return data.response;
}
