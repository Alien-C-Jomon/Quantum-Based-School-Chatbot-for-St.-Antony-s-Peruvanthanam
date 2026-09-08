import { BENCHMARKS } from "@/lib/qai/data";
import { Reveal } from "../Reveal";

const maxN = Math.max(...BENCHMARKS.map((b) => b.n));

export function BenchmarkSection() {
  return (
    <section id="benchmarks" aria-labelledby="benchmarks-title" className="snap-panel px-6 py-20">
      <div className="mx-auto w-full max-w-5xl">
        <Reveal>
          <p className="label-mono">04 — Benchmarks</p>
        </Reveal>
        <Reveal delay={60}>
          <h2
            id="benchmarks-title"
            className="mt-6 text-3xl font-semibold text-ink sm:text-4xl md:text-5xl"
          >
            Query scaling: N versus √N.
          </h2>
        </Reveal>
        <Reveal delay={120}>
          <p className="mt-4 max-w-2xl text-sm text-ink-soft">
            Theoretical query counts are the meaningful comparison. Simulator runtime is
            measured on a classical CPU and is shown only for completeness — it is not a
            speedup claim.
          </p>
        </Reveal>

        <Reveal delay={180}>
          <div className="mt-10 overflow-x-auto">
            <table className="w-full min-w-[640px] border-collapse text-left">
              <caption className="sr-only">
                Grover benchmark results by search space size
              </caption>
              <thead>
                <tr className="border-b border-hairline">
                  {[
                    "N",
                    "Qubits",
                    "Grover queries",
                    "Classical worst case",
                    "Query scaling",
                    "Success %",
                    "Sim. runtime (s)",
                  ].map((h) => (
                    <th key={h} scope="col" className="label-mono py-3 pr-4 font-normal">
                      {h}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {BENCHMARKS.map((b, i) => (
                  <tr
                    key={b.n}
                    className="border-b border-hairline transition-colors duration-300 hover:bg-quantum-soft/40"
                    style={{ ["--reveal-delay" as string]: `${i * 40}ms` }}
                  >
                    <td className="py-3 pr-4 font-mono text-sm text-ink">{b.n}</td>
                    <td className="py-3 pr-4 font-mono text-sm text-ink-soft">{b.qubits}</td>
                    <td className="py-3 pr-4 font-mono text-sm text-quantum">{b.iterations}</td>
                    <td className="py-3 pr-4 font-mono text-sm text-ink-soft">{b.classical}</td>
                    <td className="py-3 pr-4">
                      <div className="flex items-center gap-2">
                        <span
                          className="h-1.5 rounded-full bg-hairline"
                          style={{ width: `${(b.classical / maxN) * 140}px` }}
                          aria-hidden="true"
                        />
                        <span
                          className="h-1.5 rounded-full bg-quantum"
                          style={{ width: `${Math.max((b.iterations / maxN) * 140, 4)}px` }}
                          aria-hidden="true"
                        />
                      </div>
                    </td>
                    <td className="py-3 pr-4 font-mono text-sm text-ink-soft">
                      {b.success.toFixed(2)}
                    </td>
                    <td className="py-3 pr-4 font-mono text-sm text-ink-soft">
                      {b.runtime.toFixed(6)}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </Reveal>

        <Reveal delay={240}>
          <div className="mt-6 flex flex-wrap items-center gap-6">
            <span className="flex items-center gap-2 text-xs text-ink-soft">
              <span className="h-1.5 w-6 rounded-full bg-hairline" /> Classical queries (N)
            </span>
            <span className="flex items-center gap-2 text-xs text-ink-soft">
              <span className="h-1.5 w-6 rounded-full bg-quantum" /> Grover queries (≈√N)
            </span>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
