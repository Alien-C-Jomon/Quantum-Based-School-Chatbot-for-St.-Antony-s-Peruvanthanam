import { Reveal } from "../Reveal";

export function TrustSection() {
  return (
    <section id="trust" aria-labelledby="trust-title" className="snap-panel px-6">
      <div className="mx-auto w-full max-w-5xl">
        <Reveal>
          <p className="label-mono">05 — Trust</p>
        </Reveal>
        <Reveal delay={80}>
          <h2
            id="trust-title"
            className="mt-8 text-[13vw] leading-[0.9] font-semibold tracking-[-0.045em] text-ink sm:text-6xl md:text-7xl"
          >
            No verified data.
            <br />
            <span className="text-quantum">No answer.</span>
          </h2>
        </Reveal>
        <Reveal delay={160}>
          <p className="mt-10 max-w-xl text-base leading-relaxed text-ink-soft sm:text-lg">
            Q-AI answers only from verified institutional knowledge. When a question falls
            outside what the college has recorded, it says so plainly instead of inventing a
            plausible-sounding response. Honesty about the limits of the knowledge base is part
            of the design, not a failure of it.
          </p>
        </Reveal>
      </div>
    </section>
  );
}
