export type BenchmarkRow = {
  n: number;
  qubits: number;
  iterations: number;
  success: number;
  runtime: number;
  classical: number;
};

/** Verified benchmark figures from the local Qiskit Aer project run. */
export const BENCHMARKS: BenchmarkRow[] = [
  { n: 4, qubits: 2, iterations: 1, success: 100.0, runtime: 0.054349, classical: 4 },
  { n: 8, qubits: 3, iterations: 2, success: 93.65, runtime: 0.028814, classical: 8 },
  { n: 16, qubits: 4, iterations: 3, success: 95.41, runtime: 0.035617, classical: 16 },
  { n: 32, qubits: 5, iterations: 4, success: 100.0, runtime: 0.048028, classical: 32 },
  { n: 64, qubits: 6, iterations: 6, success: 99.71, runtime: 0.069978, classical: 64 },
  { n: 128, qubits: 7, iterations: 8, success: 99.61, runtime: 0.081008, classical: 128 },
  { n: 256, qubits: 8, iterations: 12, success: 100.0, runtime: 0.109565, classical: 256 },
];

export const PROJECT_FIGURES = {
  facultyRecords: 44,
  searchSpace: 64,
  qubits: 6,
  groverIterations: 6,
  queryReduction: "≈7.3×",
};

export const SCIENTIFIC_CAVEAT =
  "Qiskit Aer CPU simulation — query-complexity demonstration, not runtime speedup.";

export const KNOWLEDGE_CATEGORIES = [
  {
    id: "academics",
    title: "ACADEMICS",
    items: ["Courses", "Departments", "Syllabus"],
  },
  {
    id: "people",
    title: "PEOPLE",
    items: ["Faculty", "HODs", "Principal"],
  },
  {
    id: "achievements",
    title: "ACHIEVEMENTS",
    items: ["Ranks", "CMA", "Performances"],
  },
  {
    id: "college",
    title: "COLLEGE",
    items: ["Accreditation", "Affiliation", "Contact"],
  },
];
