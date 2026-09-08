import { Reveal } from "../Reveal";

export function WhatIsSection() {
  return (
    <section id="what" aria-labelledby="what-title" className="snap-panel px-6">
      <div className="mx-auto grid w-full max-w-5xl gap-12 md:grid-cols-12">
        <Reveal className="md:col-span-4">
          <p className="label-mono">01 — What is Q-AI?</p>
        </Reveal>
        <div className="md:col-span-8">
          <Reveal delay={80}>
            <h2
              id="what-title"
              className="text-4xl leading-[1.05] font-semibold text-ink sm:text-5xl md:text-6xl"
            >
              Your college.
              <br />
              <span className="text-ink-soft">Understood differently.</span>
            </h2>
          </Reveal>
          <Reveal delay={160}>
            <p className="mt-8 max-w-xl text-base leading-relaxed text-ink-soft sm:text-lg">
              Q-AI is a local intelligent knowledge system for St Antony&apos;s College
              Peruvanthanam. It answers questions using verified institutional information
              already held by the college — faculty records, departments, courses,
              achievements and accreditation — rather than open-ended guesswork.
            </p>
          </Reveal>
          <Reveal delay={240}>
            <dl className="mt-12 grid gap-8 border-t border-hairline pt-8 sm:grid-cols-3">
              {[
                ["Local", "Runs on college infrastructure."],
                ["Verified", "Answers trace to known records."],
                ["Focused", "Institutional knowledge only."],
              ].map(([term, desc]) => (
                <div key={term}>
                  <dt className="label-mono">{term}</dt>
                  <dd className="mt-2 text-sm text-ink">{desc}</dd>
                </div>
              ))}
            </dl>
          </Reveal>
        </div>
      </div>
    </section>
  );
}
