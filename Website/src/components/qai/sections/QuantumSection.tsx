import { PROJECT_FIGURES, SCIENTIFIC_CAVEAT } from "@/lib/qai/data";
import { Reveal } from "../Reveal";
import { QuantumOrbit } from "../QuantumOrbit";

const figures = [
  { label: "Faculty records", value: "44" },
  { label: "Search space", value: "64 states" },
  { label: "Qubits", value: "6" },
  { label: "Grover iterations", value: "6" },
];

export function QuantumSection() {
  return (
    <section id="quantum" aria-labelledby="quantum-title" className="snap-panel relative px-6">
      <QuantumOrbit className="absolute left-1/2 top-1/2 hidden w-[520px] -translate-x-1/2 -translate-y-1/2 opacity-30 lg:block" />
      <div className="relative mx-auto w-full max-w-5xl">
        <Reveal>
          <p className="label-mono">03 — Where quantum enters</p>
        </Reveal>
        <Reveal delay={60}>
          <h2
            id="quantum-title"
            className="mt-6 text-3xl font-semibold text-ink sm:text-4xl md:text-5xl"
          >
            Fewer questions asked of the data.
          </h2>
        </Reveal>

        <div className="mt-10 grid gap-4 sm:grid-cols-2">
          <Reveal delay={120}>
            <div className="h-full rounded-2xl border border-hairline bg-card p-6 shadow-soft">
              <p className="label-mono">Classical</p>
              <p className="mt-3 font-mono text-3xl text-ink">O(N)</p>
              <p className="mt-3 text-sm text-ink-soft">
                Up to {PROJECT_FIGURES.facultyRecords} record checks in the worst case — every
                entry inspected one by one.
              </p>
              <div className="mt-5 flex flex-wrap gap-1" aria-hidden="true">
                {Array.from({ length: 44 }).map((_, i) => (
                  <span key={i} className="h-2 w-2 rounded-full bg-hairline" />
                ))}
              </div>
            </div>
          </Reveal>
          <Reveal delay={200}>
            <div className="h-full rounded-2xl border border-quantum/25 bg-quantum-soft/40 p-6 shadow-soft">
              <p className="label-mono text-quantum">Grover</p>
              <p className="mt-3 font-mono text-3xl text-ink">O(√N)</p>
              <p className="mt-3 text-sm text-ink-soft">
                {PROJECT_FIGURES.groverIterations} Grover iterations over a{" "}
                {PROJECT_FIGURES.searchSpace}-state space — {PROJECT_FIGURES.queryReduction} query
                reduction for {PROJECT_FIGURES.facultyRecords} records.
              </p>
              <div className="mt-5 flex flex-wrap gap-1" aria-hidden="true">
                {Array.from({ length: 6 }).map((_, i) => (
                  <span key={i} className="animate-pulse-dot h-2 w-2 rounded-full bg-quantum" />
                ))}
              </div>
            </div>
          </Reveal>
        </div>

        <Reveal delay={260}>
          <dl className="mt-10 grid grid-cols-2 gap-6 border-t border-hairline pt-8 sm:grid-cols-4">
            {figures.map((f) => (
              <div key={f.label}>
                <dt className="label-mono">{f.label}</dt>
                <dd className="mt-1 font-mono text-lg text-ink">{f.value}</dd>
              </div>
            ))}
          </dl>
        </Reveal>

        <Reveal delay={320}>
          <p className="mt-8 max-w-2xl font-mono text-xs leading-relaxed text-ink-soft">
            {SCIENTIFIC_CAVEAT}
          </p>
        </Reveal>
      </div>
    </section>
  );
}
