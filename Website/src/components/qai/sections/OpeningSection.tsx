import { QuantumOrbit } from "../QuantumOrbit";

export function OpeningSection() {
  return (
    <section
      id="opening"
      aria-label="Introduction"
      className="snap-panel relative items-center px-6"
    >
      <QuantumOrbit className="absolute right-[-12%] top-1/2 hidden w-[46vw] max-w-[620px] -translate-y-1/2 opacity-60 md:block" />
      <div className="relative mx-auto w-full max-w-5xl">
        <p className="label-mono animate-rise">St Antony&apos;s College Peruvanthanam</p>
        <h1
          className="animate-rise mt-6 text-[22vw] leading-[0.82] font-semibold tracking-[-0.05em] text-ink sm:text-[16vw] md:text-[13rem]"
          style={{ animationDelay: "80ms" }}
        >
          Q<span className="text-quantum">-</span>AI
        </h1>
        <p
          className="animate-rise mt-8 max-w-xl font-mono text-xs tracking-[0.22em] text-ink-soft uppercase sm:text-sm"
          style={{ animationDelay: "160ms" }}
        >
          Quantum-Assisted College Intelligence
        </p>
        <div
          className="animate-rise mt-16 flex items-center gap-3"
          style={{ animationDelay: "240ms" }}
        >
          <span className="animate-drift block h-8 w-px bg-hairline" />
          <span className="label-mono">Scroll to explore</span>
        </div>
      </div>
    </section>
  );
}
