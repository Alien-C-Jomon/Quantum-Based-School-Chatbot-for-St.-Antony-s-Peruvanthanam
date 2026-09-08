import { createFileRoute } from "@tanstack/react-router";
import { OpeningSection } from "@/components/qai/sections/OpeningSection";
import { WhatIsSection } from "@/components/qai/sections/WhatIsSection";
import { KnowledgeSection } from "@/components/qai/sections/KnowledgeSection";
import { QuantumSection } from "@/components/qai/sections/QuantumSection";
import { BenchmarkSection } from "@/components/qai/sections/BenchmarkSection";
import { TrustSection } from "@/components/qai/sections/TrustSection";
import { CtaSection } from "@/components/qai/sections/CtaSection";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "Q-AI — Quantum-Assisted College Intelligence" },
      {
        name: "description",
        content:
          "Q-AI is a local, verified knowledge system for St Antony's College Peruvanthanam, with a Grover query-complexity demonstration.",
      },
      { property: "og:title", content: "Q-AI — Quantum-Assisted College Intelligence" },
      {
        property: "og:description",
        content:
          "A local intelligent knowledge system for St Antony's College Peruvanthanam. No verified data, no answer.",
      },
      { property: "og:type", content: "website" },
      { name: "twitter:card", content: "summary_large_image" },
    ],
  }),
  component: Index,
});

function Index() {
  return (
    <div className="snap-shell bg-background text-ink">
      <OpeningSection />
      <WhatIsSection />
      <KnowledgeSection />
      <QuantumSection />
      <BenchmarkSection />
      <TrustSection />
      <CtaSection />
    </div>
  );
}
