import { cn } from "@/lib/utils";

/** Restrained orbit / particle motif used as ambient decoration. */
export function QuantumOrbit({ className }: { className?: string }) {
  return (
    <div className={cn("pointer-events-none select-none", className)} aria-hidden="true">
      <div className="relative aspect-square w-full">
        <div className="animate-orbit absolute inset-0">
          <svg viewBox="0 0 200 200" className="h-full w-full">
            <ellipse
              cx="100"
              cy="100"
              rx="92"
              ry="36"
              fill="none"
              stroke="var(--quantum)"
              strokeOpacity="0.28"
            />
            <ellipse
              cx="100"
              cy="100"
              rx="36"
              ry="92"
              fill="none"
              stroke="var(--quantum)"
              strokeOpacity="0.18"
            />
            <ellipse
              cx="100"
              cy="100"
              rx="70"
              ry="70"
              fill="none"
              stroke="var(--hairline)"
            />
            <circle cx="192" cy="100" r="4" fill="var(--quantum)" />
            <circle cx="100" cy="8" r="3" fill="var(--ink-soft)" opacity="0.5" />
          </svg>
        </div>
        <div className="absolute inset-0 grid place-items-center">
          <div className="animate-pulse-dot h-2.5 w-2.5 rounded-full bg-quantum" />
        </div>
      </div>
    </div>
  );
}
