const questionInput =
    document.getElementById("question");

const askButton =
    document.getElementById("askButton");

const answerSection =
    document.getElementById("answerSection");

const answerCard =
    document.getElementById("answerCard");

const quantumSection =
    document.getElementById("quantumSection");


// --------------------------------------------------
// QUANTUM UI ELEMENTS
// --------------------------------------------------

const searchSpace =
    document.getElementById("searchSpace");

const qubits =
    document.getElementById("qubits");

const iterations =
    document.getElementById("iterations");

const successProbability =
    document.getElementById("successProbability");

const quantumStatus =
    document.getElementById("quantumStatus");

const quantumBackend =
    document.getElementById("quantumBackend");

const quantumMode =
    document.getElementById("quantumMode");

const quantumShots =
    document.getElementById("quantumShots");

const measuredIndex =
    document.getElementById("measuredIndex");

const classicalWorstCase =
    document.getElementById("classicalWorstCase");

const groverQueryCount =
    document.getElementById("groverQueryCount");

const queryReduction =
    document.getElementById("queryReduction");

const quantumMessage =
    document.getElementById("quantumMessage");


// --------------------------------------------------
// RESET QUANTUM DISPLAY
// --------------------------------------------------

function resetQuantumDisplay() {

    if (searchSpace) {
        searchSpace.textContent = "—";
    }

    if (qubits) {
        qubits.textContent = "—";
    }

    if (iterations) {
        iterations.textContent = "—";
    }

    if (successProbability) {
        successProbability.textContent = "—";
    }

    if (quantumStatus) {
        quantumStatus.textContent = "—";
    }

    if (quantumBackend) {
        quantumBackend.textContent =
            "Backend: —";
    }

    if (quantumMode) {
        quantumMode.textContent =
            "Mode: —";
    }

    if (quantumShots) {
        quantumShots.textContent =
            "Shots: —";
    }

    if (measuredIndex) {
        measuredIndex.textContent =
            "Measured index: —";
    }

    if (classicalWorstCase) {
        classicalWorstCase.textContent =
            "Classical worst case: —";
    }

    if (groverQueryCount) {
        groverQueryCount.textContent =
            "Grover query count: —";
    }

    if (queryReduction) {
        queryReduction.textContent =
            "Query reduction: —";
    }

    if (quantumMessage) {
        quantumMessage.textContent =
            "Quantum search completed.";
    }

}


// --------------------------------------------------
// DISPLAY QUANTUM RESULT
// --------------------------------------------------

function displayQuantumResult(quantum) {

    if (!quantum) {

        quantumSection.classList.add(
            "hidden"
        );

        resetQuantumDisplay();

        return;
    }


    quantumSection.classList.remove(
        "hidden"
    );


    // --------------------------------------------------
    // SEARCH SPACE
    // --------------------------------------------------

    if (searchSpace) {

        searchSpace.textContent =
            quantum.search_space ?? "—";

    }


    // --------------------------------------------------
    // QUBITS
    // --------------------------------------------------

    if (qubits) {

        qubits.textContent =
            quantum.qubits ?? "—";

    }


    // --------------------------------------------------
    // GROVER ITERATIONS
    // --------------------------------------------------

    if (iterations) {

        iterations.textContent =
            quantum.grover_iterations ?? "—";

    }


    // --------------------------------------------------
    // SUCCESS PROBABILITY
    // --------------------------------------------------

    if (successProbability) {

        if (
            typeof quantum.success_probability ===
            "number"
        ) {

            successProbability.textContent =
                `${(
                    quantum.success_probability * 100
                ).toFixed(2)}%`;

        } else {

            successProbability.textContent =
                "—";

        }

    }


    // --------------------------------------------------
    // TARGET STATUS
    // --------------------------------------------------

    if (quantumStatus) {

        quantumStatus.textContent =
            quantum.success
                ? "FOUND"
                : "NOT FOUND";

        quantumStatus.classList.toggle(
            "success",
            Boolean(quantum.success)
        );

    }


    // --------------------------------------------------
    // BACKEND
    // --------------------------------------------------

    if (quantumBackend) {

        quantumBackend.textContent =
            `Backend: ${
                quantum.backend ?? "—"
            }`;

    }


    // --------------------------------------------------
    // MODE
    // --------------------------------------------------

    if (quantumMode) {

        quantumMode.textContent =
            `Mode: ${
                quantum.mode ?? "—"
            }`;

    }


    // --------------------------------------------------
    // SHOTS
    // --------------------------------------------------

    if (quantumShots) {

        quantumShots.textContent =
            `Shots: ${
                quantum.shots ?? "—"
            }`;

    }


    // --------------------------------------------------
    // MEASURED INDEX
    // --------------------------------------------------

    if (measuredIndex) {

        measuredIndex.textContent =
            `Measured index: ${
                quantum.measured_index ?? "—"
            }`;

    }


    // --------------------------------------------------
    // CLASSICAL WORST CASE
    // --------------------------------------------------

    if (classicalWorstCase) {

        classicalWorstCase.textContent =
            `Classical worst case: ${
                quantum.classical_worst_case ?? "—"
            } candidate checks`;

    }


    // --------------------------------------------------
    // GROVER QUERY COUNT
    // --------------------------------------------------

    if (groverQueryCount) {

        groverQueryCount.textContent =
            `Grover query count: ${
                quantum.grover_query_count ?? "—"
            }`;

    }


    // --------------------------------------------------
    // QUERY REDUCTION
    // --------------------------------------------------

    if (queryReduction) {

        if (
            typeof quantum.query_reduction_factor ===
            "number"
        ) {

            queryReduction.textContent =
                `Query reduction: ${
                    quantum.query_reduction_factor.toFixed(2)
                }×`;

        } else {

            queryReduction.textContent =
                "Query reduction: —";

        }

    }


    // --------------------------------------------------
    // FINAL QUANTUM MESSAGE
    // --------------------------------------------------

    if (quantumMessage) {

        if (quantum.success) {

            quantumMessage.textContent =
                "Grover search successfully identified the target candidate.";

        } else {

            quantumMessage.textContent =
                "Grover search did not identify the target candidate.";

        }

    }

}


// --------------------------------------------------
// ASK Q-AI
// --------------------------------------------------

async function askQAI() {

    const question =
        questionInput.value.trim();


    // --------------------------------------------------
    // EMPTY QUESTION
    // --------------------------------------------------

    if (!question) {

        answerSection.classList.remove(
            "hidden"
        );

        answerCard.textContent =
            "❌ Please enter a question.";

        quantumSection.classList.add(
            "hidden"
        );

        resetQuantumDisplay();

        return;
    }


    // --------------------------------------------------
    // LOADING STATE
    // --------------------------------------------------

    askButton.disabled = true;

    const buttonText =
        askButton.querySelector("span");

    if (buttonText) {

        buttonText.textContent =
            "Thinking...";

    }


    answerSection.classList.remove(
        "hidden"
    );

    answerCard.textContent =
        "⚛️ Q-AI is processing your question...";

    quantumSection.classList.add(
        "hidden"
    );

    resetQuantumDisplay();


    // --------------------------------------------------
    // API REQUEST
    // --------------------------------------------------

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/api/ask",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    question: question
                })
            }
        );


        // --------------------------------------------------
        // HTTP STATUS
        // --------------------------------------------------

        if (!response.ok) {

            throw new Error(
                `API returned HTTP ${response.status}`
            );

        }


        const data =
            await response.json();


        // --------------------------------------------------
        // API ERROR
        // --------------------------------------------------

        if (!data.success) {

            answerCard.textContent =
                "❌ " +
                (
                    data.error ||
                    "Something went wrong."
                );

            quantumSection.classList.add(
                "hidden"
            );

            return;
        }


        // --------------------------------------------------
        // VERIFIED ANSWER
        // --------------------------------------------------

        answerCard.textContent =
            data.answer;


        // --------------------------------------------------
        // QUANTUM RESULT
        // --------------------------------------------------

        displayQuantumResult(
            data.quantum
        );


    } catch (error) {

        console.error(
            "Q-AI API Error:",
            error
        );


        answerCard.textContent =
            "❌ Q-AI could not connect to the local API.\n\n" +
            "Make sure api.py is running.";


        quantumSection.classList.add(
            "hidden"
        );

        resetQuantumDisplay();

    }


    // --------------------------------------------------
    // RESET BUTTON
    // --------------------------------------------------

    finally {

        askButton.disabled = false;


        if (buttonText) {

            buttonText.textContent =
                "Ask Q-AI";

        }

    }

}


// --------------------------------------------------
// BUTTON CLICK
// --------------------------------------------------

askButton.addEventListener(
    "click",
    askQAI
);


// --------------------------------------------------
// ENTER KEY
// --------------------------------------------------

questionInput.addEventListener(
    "keydown",
    function(event) {

        if (
            event.key === "Enter" &&
            !event.shiftKey
        ) {

            event.preventDefault();

            askQAI();

        }

    }
);