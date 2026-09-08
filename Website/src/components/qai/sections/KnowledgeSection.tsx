import { KNOWLEDGE_CATEGORIES } from "@/lib/qai/data";
import { Reveal } from "../Reveal";

export function KnowledgeSection() {
  return (
    <section id="knowledge" aria-labelledby="knowledge-title" className="snap-panel px-6">
      <div className="mx-auto w-full max-w-5xl">
        <Reveal>
          <p className="label-mono">02 — The Knowledge</p>
        </Reveal>
        <Reveal delay={60}>
          <h2
            id="knowledge-title"
            className="mt-6 text-3xl font-semibold text-ink sm:text-4xl md:text-5xl"
          >
            Four domains of verified college knowledge.
          </h2>
        </Reveal>
        <ul className="mt-12 divide-y divide-hairline border-y border-hairline">
          {KNOWLEDGE_CATEGORIES.map((cat, i) => (
            <Reveal as="li" key={cat.id} delay={100 + i * 80}>
              <div className="group grid gap-3 py-6 transition-colors duration-300 hover:bg-quantum-soft/50 sm:grid-cols-12 sm:items-baseline sm:px-4">
                <span className="label-mono sm:col-span-1">{`0${i + 1}`}</span>
                <h3 className="text-xl font-semibold tracking-tight text-ink transition-transform duration-300 group-hover:translate-x-1 sm:col-span-4 sm:text-2xl">
                  {cat.title}
                </h3>
                <div className="flex flex-wrap gap-x-6 gap-y-2 sm:col-span-7">
                  {cat.items.map((item) => (
                    <span key={item} className="text-sm text-ink-soft">
                      {item}
                    </span>
                  ))}
                </div>
              </div>
            </Reveal>
          ))}
        </ul>
      </div>
    </section>
  );
}
