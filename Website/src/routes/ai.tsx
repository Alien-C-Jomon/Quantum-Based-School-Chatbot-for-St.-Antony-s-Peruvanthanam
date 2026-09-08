import { createFileRoute, Link } from "@tanstack/react-router";
import { useEffect, useRef, useState } from "react";
import { askQAI, checkStatus, ApiUnavailableError, type QuantumResult } from "@/lib/qai/api";
import { QuantumPanel } from "@/components/qai/QuantumPanel";
import { QuantumOrbit } from "@/components/qai/QuantumOrbit";

export const Route = createFileRoute("/ai")({
  head: () => ({
    meta: [
      { title: "Ask Q-AI — St Antony's College Peruvanthanam" },
      {
        name: "description",
        content:
          "Ask Q-AI about faculty, departments, courses, achievements and accreditation at St Antony's College Peruvanthanam.",
      },
      { property: "og:title", content: "Ask Q-AI — St Antony's College" },
      {
        property: "og:description",
        content: "A local, verified knowledge assistant for St Antony's College Peruvanthanam.",
      },
      { property: "og:type", content: "website" },
      { name: "twitter:card", content: "summary_large_image" },
    ],
  }),
  component: AiPage,
});

type Message = {
  id: string;
  role: "user" | "qai";
  text: string;
  quantum?: QuantumResult;
  error?: boolean;
};

function AiPage() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [pending, setPending] = useState(false);
  const [status, setStatus] = useState<"checking" | "online" | "offline">("checking");
  const listEndRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const controller = new AbortController();
    checkStatus(controller.signal).then((ok) => setStatus(ok ? "online" : "offline"));
    return () => controller.abort();
  }, []);

  useEffect(() => {
    listEndRef.current?.scrollIntoView({ block: "end" });
  }, [messages, pending]);

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    const question = input.trim();
    if (!question || pending) return;

    const userMessage: Message = { id: crypto.randomUUID(), role: "user", text: question };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setPending(true);

    try {
      const result = await askQAI(question);
      setStatus("online");
      setMessages((prev) => [
        ...prev,
        {
          id: crypto.randomUUID(),
          role: "qai",
          text: result.answer,
          ...(result.quantum ? { quantum: result.quantum } : {}),
        },
      ]);
    } catch (error) {
      const unavailable = error instanceof ApiUnavailableError;
      if (unavailable) setStatus("offline");
      setMessages((prev) => [
        ...prev,
        {
          id: crypto.randomUUID(),
          role: "qai",
          error: true,
          text: unavailable
            ? "The local Q-AI service isn't reachable from here, so there is no verified answer to show. Start the local Q-AI service and ask again."
            : error instanceof Error
              ? error.message
              : "Something went wrong while contacting Q-AI.",
        },
      ]);
    } finally {
      setPending(false);
    }
  }

  const empty = messages.length === 0;

  return (
    <div className="flex min-h-dvh flex-col bg-background">
      <header className="sticky top-0 z-20 border-b border-hairline bg-background/85 backdrop-blur">
        <div className="mx-auto flex w-full max-w-3xl items-center justify-between gap-4 px-6 py-4">
          <div className="flex items-baseline gap-3">
            <span className="text-lg font-semibold tracking-tight text-ink">
              Q<span className="text-quantum">-</span>AI
            </span>
            <span className="hidden text-xs text-ink-soft sm:inline">
              St Antony&apos;s College
            </span>
          </div>
          <div className="flex items-center gap-4">
            <span className="label-mono flex items-center gap-2">
              <span
                className={`h-1.5 w-1.5 rounded-full ${
                  status === "online"
                    ? "animate-pulse-dot bg-quantum"
                    : status === "checking"
                      ? "bg-hairline"
                      : "bg-ink-soft"
                }`}
                aria-hidden="true"
              />
              Verified • Local
            </span>
            <Link
              to="/"
              className="label-mono rounded-full border border-hairline px-3 py-1.5 transition-colors duration-300 hover:bg-quantum-soft/60"
            >
              Back
            </Link>
          </div>
        </div>
      </header>

      <main className="mx-auto flex w-full max-w-3xl flex-1 flex-col px-6">
        {empty ? (
          <div className="relative flex flex-1 flex-col items-center justify-center py-20 text-center">
            <QuantumOrbit className="pointer-events-none absolute top-1/2 left-1/2 w-[70vw] max-w-[420px] -translate-x-1/2 -translate-y-1/2 opacity-25" />
            <h1 className="animate-rise relative text-4xl leading-tight font-semibold text-ink sm:text-5xl">
              Ask anything about your college.
            </h1>
            <p
              className="animate-rise relative mt-5 max-w-md text-sm text-ink-soft sm:text-base"
              style={{ animationDelay: "100ms" }}
            >
              Faculty, departments, courses, achievements, accreditation and more.
            </p>
            {status === "offline" && (
              <p className="relative mt-8 max-w-md rounded-xl border border-hairline bg-card px-4 py-3 text-xs text-ink-soft">
                The local Q-AI service isn&apos;t reachable from this preview. The interface is
                ready — answers appear once the local service is running on this machine.
              </p>
            )}
          </div>
        ) : (
          <ul className="flex-1 space-y-6 py-10" aria-live="polite">
            {messages.map((m) => (
              <li key={m.id} className="animate-rise">
                {m.role === "user" ? (
                  <div className="flex justify-end">
                    <p className="max-w-[85%] rounded-2xl rounded-br-md bg-ink px-4 py-3 text-sm text-primary-foreground">
                      {m.text}
                    </p>
                  </div>
                ) : (
                  <div className="max-w-[92%]">
                    <p className="label-mono">Q-AI</p>
                    <p
                      className={`mt-2 text-sm leading-relaxed whitespace-pre-wrap ${
                        m.error ? "text-ink-soft" : "text-ink"
                      }`}
                    >
                      {m.text}
                    </p>
                    {m.quantum && <QuantumPanel quantum={m.quantum} />}
                  </div>
                )}
              </li>
            ))}
            {pending && (
              <li className="label-mono flex items-center gap-2">
                <span className="animate-pulse-dot h-1.5 w-1.5 rounded-full bg-quantum" />
                Searching verified knowledge
              </li>
            )}
            <div ref={listEndRef} />
          </ul>
        )}
      </main>

      <div className="sticky bottom-0 border-t border-hairline bg-background/90 backdrop-blur">
        <form onSubmit={handleSubmit} className="mx-auto w-full max-w-3xl px-6 py-5">
          <label htmlFor="qai-input" className="sr-only">
            Ask a question about St. Antony&apos;s College
          </label>
          <div className="flex items-center gap-2 rounded-full border border-hairline bg-card px-2 py-2 shadow-soft transition-shadow duration-300 focus-within:shadow-lift">
            <input
              id="qai-input"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask a question about St. Antony's College..."
              autoComplete="off"
              className="min-w-0 flex-1 bg-transparent px-4 py-2 text-sm text-ink placeholder:text-ink-soft focus:outline-none"
            />
            <button
              type="submit"
              disabled={pending || input.trim() === ""}
              className="rounded-full bg-ink px-5 py-2.5 font-mono text-[11px] tracking-[0.18em] text-primary-foreground uppercase transition-opacity duration-300 disabled:opacity-35"
            >
              {pending ? "…" : "Send"}
            </button>
          </div>
          <p className="mt-3 text-center font-mono text-[10px] tracking-wide text-ink-soft">
            Answers come only from verified local college data.
          </p>
        </form>
      </div>
    </div>
  );
}
