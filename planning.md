# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---


## Domain
Q:[What domain did you choose? Why is this knowledge valuable and hard to find through official channels?]

 A Computer Science major survival guide and tip, compiled from various Reddit sources. The information is based off of questions about how to become a better CS student or alumnus, providing helpful insights for learning from your classes and securing a job.

---
Q: [List your specific sources: URLs, subreddit names, forum threads, or file descriptions. Aim for variety — sources that together cover different subtopics or perspectives within your domain.]

 ## Documents
| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 |r/learningprogramming|"How to be a successful CS major?"|https://www.reddit.com/r/learnprogramming/comments/1jmz8ms/how_to_be_a_successful_cs_major/|                 
| 2 |r/learningprogramming |"How do I prepare for Computer Science major?"|https://www.reddit.com/r/learnprogramming/comments/11dgi45/how_do_i_prepare_for_computer_science_major/|
| 3 |r/cscareerquestions|"finishing a CS degree faster ? how ? send help ?"|https://www.reddit.com/r/cscareerquestions/comments/pro1td/finishing_a_cs_degree_faster_how_send_help/|
| 4 |r/learningprogramming|"How Hard Is It To Complete a Computer Science Degree"
|https://www.reddit.com/r/learnprogramming/comments/1foktfc/how_hard_is_it_to_complete_a_computer_science/|
| 5 |r/learningprogramming|"What's the best way to prepare myself for a degree in computer science?"|https://www.reddit.com/r/learnprogramming/comments/951xmkwhats_the_best_way_to_prepare_myself_for_a_degree/|
| 6 |r/learningprogramming|"How can i further my computer science skills and help set up a career?"|https://www.reddit.com/r/learnprogramming/comments/smwl5y/how_can_i_further_my_computer_science_skills_and/ |
| 7 |r/cscareerquestions|"What should a CS student be learning outside of the classroom?"
| https://www.reddit.com/r/cscareerquestions/comments/1fnikk9/what_should_a_cs_student_be_learning_outside_of/|
| 8 |r/learningprogramming|Finished my CS degree and know nothing about programming.
 |https://www.reddit.com/r/learnprogramming/comments/1f9s8xr/finished_my_cs_degree_and_know_nothing_about/|
| 9 |r/learningprogramming|"How Can I Develop Practical Skills for a Computer Science Job?"
 |https://www.reddit.com/r/learnprogramming/comments/1hbziw0/how_can_i_develop_practical_skills_for_a_computer/|
| 10 |r/cscareerquestions|"Just graduated, no experience or projects, how do I prepare to break into the industry?"
 |https://www.reddit.com/r/cscareerquestions/comments/zp4gln/just_graduated_no_experience_or_projects_how_do_i/|

---
## Chunking Strategy 
 How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ.

**Chunk size:**
500 characters: Reddit comments usually range from 2-5 sentences which transates to around 400 characters. That way with 500 we can capture one chunk of the paragraph without fragmenting the data by cutting the idea the redditor was conveying.
**Overlap:**
50 characters is a half an entire sentence. So 50 assures we are saving a possible thought/explanation split from two different chunks.
**Reasoning:**
Reddit threads are medium-short form answers that are usually answered in the first 500 characters. Bigger chunks would allow a mix of different opinions into a single thought making retrieveal for specific answers less relevant.Smaller ones would split comments before they completed their thought.

## Retrieval Approach

  Q Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)? AKA: Which tool that converts chunks into numbers.

    Q How many chunks will you retrieve per query (top-k)? 5 chunks per query. Better for not overwhelming the LLM and not going over the 512 token limit.

  Q   If you were deploying this for real users and cost wasn't a constraint, what tradeoffs would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? --> 

**Embedding model:**
all-MiniLM-L6-v2 via sentence-transformers, it's free and quick converter, runs locally with no API key needed for the model.

**Top-k:**
Top-k: Keeps the relevant pool of information and restricts the model to only pick those it ranks as most similar to the query. Causing the model to ignore all other possiblities and non relevant chunks. Our query of 5 makes our answers be as safe and not overwhelming the LLM. A higher k 50 to 100 is for larger diverse choices, making it less relevant to the question asked. 

**Production tradeoff reflection:**
If cost wasn't a problem I'd consider OpenAI's text-embedding-3-large model. It scores high on accuracy benchmarks and supports up to 8,000 tokens per chunk as oppsed to 512 for the local model. The tradeoff is cost since you pay per token, and time-latency since every query needs an API call. Multilingual support isn't needed here since all my documents are in English and less relevant.


## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 |What would you suggest I do to prep for interviews? | |
| 2 |How can I become a more efficent programmer | |
| 3 |How long is the CS major program| |
| 4 | | |
| 5 | | |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1.

2.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
