# Quantum College Companion

Build a polished two-page frontend for a project called Q-AI: Quantum-Assisted College Intelligence for St Antony's College Peruvanthanam. This is a frontend-only experience; do not invent backend data or require a cloud database. The user's existing local backend is Flask at http://127.0.0.1:5000/api/ask and /api/status, but the current local Python/Qiskit backend, knowledge base, tests, and benchmark files must remain untouched and are not available in this project. Build the UI so the chatbot can later connect to that existing local API, with a clearly isolated API base constant.

DESIGN DIRECTION: white/light, premium, minimal, editorial, clean, sophisticated technology product. Avoid cyberpunk, dark neon, excessive glassmorphism, excessive gradients, clutter, and generic admin dashboards. Use near-black typography, soft gray secondary text, one restrained quantum accent, generous whitespace, subtle depth, smooth motion, and responsive behavior.

PAGE 1 LANDING: create full-screen section-by-section snap scrolling inspired by the interaction concept of https://webflow-scroll-snap.webflow.io/#four, but with original design/content. Sections: (1) Opening: huge Q-AI, subtitle QUANTUM-ASSISTED COLLEGE INTELLIGENCE, St Antony's College Peruvanthanam, SCROLL TO EXPLORE. (2) What is Q-AI?: 'Your college. Understood differently.' and a concise explanation that it is a local intelligent knowledge system using verified institutional information. (3) The Knowledge: elegant animated categories ACADEMICS (Courses, Departments, Syllabus), PEOPLE (Faculty, HODs, Principal), ACHIEVEMENTS (Ranks, CMA, Performances), COLLEGE (Accreditation, Affiliation, Contact). (4) Where Quantum Enters: major visual section showing CLASSICAL O(N) versus GROVER O(√N), with current verified project figures: 44 faculty records, 64-state quantum search space, 6 qubits, 6 Grover iterations, approximately 7.3x query reduction for 44 records. Include exact scientific caveat: 'Qiskit Aer CPU simulation — query-complexity demonstration, not runtime speedup.' Never claim simulator runtime speedup. (5) Benchmarks: use these verified benchmark rows as data for a visual scaling section: N=4 qubits=2 iterations=1 success=100.00 runtime=0.054349 classical=4; N=8 qubits=3 iterations=2 success=93.65 runtime=0.028814 classical=8; N=16 qubits=4 iterations=3 success=95.41 runtime=0.035617 classical=16; N=32 qubits=5 iterations=4 success=100.00 runtime=0.048028 classical=32; N=64 qubits=6 iterations=6 success=99.71 runtime=0.069978 classical=64; N=128 qubits=7 iterations=8 success=99.61 runtime=0.081008 classical=128; N=256 qubits=8 iterations=12 success=100.00 runtime=0.109565 classical=256. Visualize query scaling clearly as N versus sqrt(N); distinguish theoretical query counts from simulator runtime. (6) Trust: large statement 'NO VERIFIED DATA. NO ANSWER.' Explain Q-AI should only answer from verified knowledge and explicitly say when information is unavailable rather than hallucinate. (7) Final CTA: 'READY TO ASK?' / 'Explore St Antony's College with Q-AI.' Button ENTER Q-AI → navigating to /ai.

PAGE 2 /ai CHAT: inspired by the minimalist interaction concept of https://rollix-bot.webflow.io/ but completely original Q-AI styling. Same white/light design language and animation system. Header: Q-AI, St Antony's College, status VERIFIED • LOCAL, back to landing. Center headline 'Ask anything about your college.' Supporting text: 'Faculty, departments, courses, achievements, accreditation and more.' Replace the reference site's email interaction with a clean chat input whose placeholder is 'Ask a question about St. Antony's College...' and send interaction. Render user messages and Q-AI responses. When backend data contains quantum information, show a compact secondary quantum result with search space, qubits, Grover iterations, success probability, measured index, classical worst case, Grover query count, query reduction, backend, and simulation mode. Build an API service abstraction with API_BASE = 'http://127.0.0.1:5000' and call /api/ask; do not mock responses in the actual chat flow. Handle API unavailable state elegantly. Since this hosted Lovable preview cannot reach the user's local machine reliably, keep the integration configurable and make the UI fully functional structurally without inventing live responses.

ANIMATION: subtle fade/translate, text reveals, gentle scale, restrained quantum particle/orbit motif, smooth snap transitions, elegant hover/focus states. Do not make motion slow or distracting. Include accessibility: keyboard navigation, visible focus, reduced-motion support, semantic headings/buttons, good contrast. Make mobile layouts excellent.

Use React/TypeScript/Tailwind as appropriate. Keep components organized and reusable. Add no authentication, database, paid APIs, or unnecessary dependencies. The goal is to create the polished frontend experience first while preserving scientific honesty and the user's existing local Q-AI architecture.

This project was built with [Lovable](https://lovable.dev).

## Build with Lovable

Continue developing this project in the [Lovable editor](https://lovable.dev/projects/264a1d7b-2cfa-4938-a748-2edaeb45c660).

- **Ship faster**: describe what you want to build and Lovable handles the code.
- **Stay in sync**: every change made in Lovable is committed straight to this repository.
- **Full ownership**: this code is yours. Push to `main` on GitHub and your changes sync back into Lovable, ready for your next prompt.

## Development

Prefer working locally? You need Node.js and npm — [install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating).

```sh
git clone <this-repository-url>
cd <repository-name>
npm i
npm run dev
```
