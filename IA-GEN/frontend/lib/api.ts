const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

interface ApiErrorPayload {
  success?: boolean;
  detail?: string;
  error?: {
    code?: string;
    message?: string;
    retryable?: boolean;
  };
}

interface ApiErrorOptions {
  status: number;
  message: string;
  code?: string;
  retryable?: boolean;
}

export class ApiError extends Error {
  readonly status: number;
  readonly code: string;
  readonly retryable: boolean;

  constructor({
    status,
    message,
    code = "API_ERROR",
    retryable = false,
  }: ApiErrorOptions) {
    super(message);

    this.name = "ApiError";
    this.status = status;
    this.code = code;
    this.retryable = retryable;
  }
}

async function parseErrorPayload(
  response: Response
): Promise<ApiErrorPayload | null> {
  try {
    return (await response.json()) as ApiErrorPayload;
  } catch {
    return null;
  }
}

export async function apiFetch<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<T> {
  const headers = new Headers(options.headers);

  const isFormData =
    typeof FormData !== "undefined" && options.body instanceof FormData;

  if (options.body && !isFormData && !headers.has("Content-Type")) {
    headers.set("Content-Type", "application/json");
  }

  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    ...options,
    headers,
  });

  if (!response.ok) {
    const payload = await parseErrorPayload(response);

    throw new ApiError({
      status: response.status,
      code: payload?.error?.code ?? "API_ERROR",
      message:
        payload?.error?.message ??
        payload?.detail ??
        "No fue posible completar la solicitud.",
      retryable: payload?.error?.retryable ?? false,
    });
  }

  if (response.status === 204) {
    return undefined as T;
  }

  return response.json() as Promise<T>;
}
