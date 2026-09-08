import { Link } from "@tanstack/react-router";
import { Reveal } from "../Reveal";
import { QuantumOrbit } from "../QuantumOrbit";

export function CtaSection() {
  return (
    <section id="cta" aria-labelledby="cta-title" className="snap-panel relative px-6">
      <QuantumOrbit className="absolute left-1/2 top-1/2 w-[80vw] max-w-[560px] -translate-x-1/2 -translate-y-1/2 opacity-25" />
      <div className="relative mx-auto w-full max-w-3xl text-center">
        <Reveal>
          <h2
            id="cta-title"
            className="text-[14vw] leading-[0.9] font-semibold tracking-[-0.045em] text-ink sm:text-6xl md:text-7xl"
          >
            Ready to ask?
          </h2>
        </Reveal>
        <Reveal delay={100}>
          <p className="mt-6 text-base text-ink-soft sm:text-lg">
            Explore St Antony&apos;s College with Q-AI.
          </p>
        </Reveal>
        <Reveal delay={180}>
          <Link
            to="/ai"
            className="mt-12 inline-flex items-center gap-3 rounded-full bg-ink px-8 py-4 font-mono text-xs tracking-[0.22em] text-primary-foreground uppercase transition-all duration-300 hover:gap-5 hover:shadow-lift"
          >
            Enter Q-AI
            <span aria-hidden="true">→</span>
          </Link>
        </Reveal>
      </div>
    </section>
  );
}
