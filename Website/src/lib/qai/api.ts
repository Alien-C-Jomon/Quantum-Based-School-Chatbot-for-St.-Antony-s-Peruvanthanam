/**
 * Isolated API layer for the user's existing local Q-AI Flask backend.
 * Nothing here is mocked — if the local backend is unreachable, callers
 * receive an explicit unavailable state instead of invented data.
 */
export const API_BASE = "http://127.0.0.1:5000";

export const ASK_ENDPOINT = "/api/ask";
export const STATUS_ENDPOINT = "/api/status";

export type QuantumResult = {
  searchSpace: number | undefined;
  qubits: number | undefined;
  iterations: number | undefined;
  successProbability: number | undefined;
  measuredIndex: number | undefined;
  classicalWorstCase: number | undefined;
  groverQueries: number | undefined;
  queryReduction: string | undefined;
  backend: string | undefined;
  simulationMode: string | undefined;
};

export type AskResult = {
  answer: string;
  quantum: QuantumResult | undefined;
};

export class ApiUnavailableError extends Error {
  constructor(message = "Local Q-AI backend is unreachable.") {
    super(message);
    this.name = "ApiUnavailableError";
  }
}

function num(...values: unknown[]): number | undefined {
  for (const v of values) {
    if (typeof v === "number" && Number.isFinite(v)) return v;
    if (typeof v === "string" && v.trim() !== "" && Number.isFinite(Number(v))) return Number(v);
  }
  return undefined;
}

function str(...values: unknown[]): string | undefined {
  for (const v of values) {
    if (typeof v === "string" && v.trim() !== "") return v;
    if (typeof v === "number") return String(v);
  }
  return undefined;
}

/** Normalises the variety of key spellings a local backend may return. */
export function parseQuantum(raw: unknown): QuantumResult | undefined {
  if (!raw || typeof raw !== "object") return undefined;
  const q = raw as Record<string, unknown>;
  const result: QuantumResult = {
    searchSpace: num(q["search_space"], q["searchSpace"], q["N"]),
    qubits: num(q["qubits"], q["num_qubits"]),
    iterations: num(q["iterations"], q["grover_iterations"], q["groverIterations"]),
    successProbability: num(
      q["success_probability"],
      q["successProbability"],
      q["success"],
    ),
    measuredIndex: num(q["measured_index"], q["measuredIndex"], q["index"]),
    classicalWorstCase: num(
      q["classical_worst_case"],
      q["classicalWorstCase"],
      q["classical"],
    ),
    groverQueries: num(q["grover_queries"], q["groverQueries"], q["queries"]),
    queryReduction: str(q["query_reduction"], q["queryReduction"], q["speedup"]),
    backend: str(q["backend"], q["device"]),
    simulationMode: str(q["simulation_mode"], q["simulationMode"], q["mode"]),
  };
  return Object.values(result).some((v) => v !== undefined) ? result : undefined;
}

export async function askQAI(question: string, signal?: AbortSignal): Promise<AskResult> {
  let response: Response;
  try {
    response = await fetch(`${API_BASE}${ASK_ENDPOINT}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, query: question }),
      signal: signal ?? null,
    });
  } catch {
    throw new ApiUnavailableError();
  }

  if (!response.ok) {
    throw new Error(`Backend responded with ${response.status}.`);
  }

  const data = (await response.json()) as Record<string, unknown>;
  const answer =
    str(data["answer"], data["response"], data["result"], data["message"]) ??
    "The backend returned no answer text.";

  return {
    answer,
    quantum: parseQuantum(data["quantum"] ?? data["quantum_result"] ?? data),
  };
}

export type BackendStatus = "checking" | "online" | "offline";

export async function checkStatus(signal?: AbortSignal): Promise<boolean> {
  try {
    const res = await fetch(`${API_BASE}${STATUS_ENDPOINT}`, { signal: signal ?? null });
    return res.ok;
  } catch {
    return false;
  }
}
