import type { QuantumResult } from "@/lib/qai/api";
import { SCIENTIFIC_CAVEAT } from "@/lib/qai/data";

function Row({ label, value }: { label: string; value: string | number | undefined }) {
  if (value === undefined || value === "") return null;
  return (
    <div className="flex items-baseline justify-between gap-4 py-1.5">
      <dt className="label-mono">{label}</dt>
      <dd className="font-mono text-xs text-ink">{value}</dd>
    </div>
  );
}

export function QuantumPanel({ quantum }: { quantum: QuantumResult }) {
  return (
    <details className="mt-3 rounded-xl border border-quantum/25 bg-quantum-soft/40 px-4 py-3">
      <summary className="label-mono cursor-pointer text-quantum select-none">
        Quantum result
      </summary>
      <dl className="mt-2 divide-y divide-hairline">
        <Row label="Search space" value={quantum.searchSpace} />
        <Row label="Qubits" value={quantum.qubits} />
        <Row label="Grover iterations" value={quantum.iterations} />
        <Row
          label="Success probability"
          value={
            quantum.successProbability === undefined
              ? undefined
              : `${quantum.successProbability}`
          }
        />
        <Row label="Measured index" value={quantum.measuredIndex} />
        <Row label="Classical worst case" value={quantum.classicalWorstCase} />
        <Row label="Grover queries" value={quantum.groverQueries} />
        <Row label="Query reduction" value={quantum.queryReduction} />
        <Row label="Backend" value={quantum.backend} />
        <Row label="Simulation mode" value={quantum.simulationMode} />
      </dl>
      <p className="mt-3 font-mono text-[10px] leading-relaxed text-ink-soft">
        {SCIENTIFIC_CAVEAT}
      </p>
    </details>
  );
}
