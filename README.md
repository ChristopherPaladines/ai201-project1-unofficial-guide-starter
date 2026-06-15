# The Unofficial Guide — Project 1

---

## Domain

CS major survival tips collected from Reddit threads. This covers real student advice on how to succeed in a CS degree, what to learn outside of class, and how to break into the industry after graduating. This knowledge is valuable because it reflects honest student experiences — not the polished information universities put on their websites. Official sources won t tell you how hard Data Structures really is or what skills actually get you hired.

---

## Document Sources

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | r/learnprogramming | Reddit thread | https://www.reddit.com/r/learnprogramming/comments/1jmz8ms/how_to_be_a_successful_cs_major/ |
| 2 | r/learnprogramming | Reddit thread | https://www.reddit.com/r/learnprogramming/comments/11dgi45/how_do_i_prepare_for_computer_science_major/ |
| 3 | r/cscareerquestions | Reddit thread | https://www.reddit.com/r/cscareerquestions/comments/pro1td/finishing_a_cs_degree_faster_how_send_help/ |
| 4 | r/learnprogramming | Reddit thread | https://www.reddit.com/r/learnprogramming/comments/1foktfc/how_hard_is_it_to_complete_a_computer_science/ |
| 5 | r/learnprogramming | Reddit thread | https://www.reddit.com/r/learnprogramming/comments/951xmk/whats_the_best_way_to_prepare_myself_for_a_degree/ |
| 6 | r/learnprogramming | Reddit thread | https://www.reddit.com/r/learnprogramming/comments/smwl5y/how_can_i_further_my_computer_science_skills_and/ |
| 7 | r/cscareerquestions | Reddit thread | https://www.reddit.com/r/cscareerquestions/comments/1fnikk9/what_should_a_cs_student_be_learning_outside_of/ |
| 8 | r/learnprogramming | Reddit thread | https://www.reddit.com/r/learnprogramming/comments/1f9s8xr/finished_my_cs_degree_and_know_nothing_about/ |
| 9 | r/learnprogramming | Reddit thread | https://www.reddit.com/r/learnprogramming/comments/1hbziw0/how_can_i_develop_practical_skills_for_a_computer/ |
| 10 | r/cscareerquestions | Reddit thread | https://www.reddit.com/r/cscareerquestions/comments/zp4gln/just_graduated_no_experience_or_projects_how_do_i/ |

---

## Chunking Strategy

**Chunk size:** 500 characters. Reddit comments usually range from 2-5 sentences which translates to around 400 characters. 500 characters captures one complete comment without cutting the idea mid-thought.

**Overlap:** 50 characters, which is roughly half a sentence. This ensures that if a thought gets split across two chunks, the second chunk still has enough context to make sense on its own.

**Why these choices fit your documents:** Reddit threads are made up of short opinion-based comments. Bigger chunks would mix multiple peoples opinions into one chunk making retrieval less specific. Smaller chunks would split comments before they completed their thought.

**Final chunk count:** 59 chunks across 11 documents.

---

## Embedding Model

**Model used:** all-MiniLM-L6-v2 via sentence-transformers. Runs locally with no API key or rate limits needed.

**Production tradeoff reflection:** If cost was not a constraint I would consider OpenAI text-embedding-3-large. It scores higher on accuracy benchmarks like MTEB and supports up to 8000 tokens per chunk compared to 512 for the local model. The tradeoff is cost since you pay per token and latency since every query needs an API call. Multilingual support is not needed since all documents are in English.

---

## Grounded Generation

**System prompt grounding instruction:** You are a helpful assistant for CS students. Answer questions using ONLY the provided context from Reddit threads. If the context does not contain enough information say I dont have enough information on that. Always cite which document your answer comes from.

**How source attribution is surfaced in the response:** The top 5 retrieved chunk sources are displayed in a separate Sources box in the Gradio UI after every response. The LLM is also instructed to cite sources inline in its answer.

---

## Sample Chunks

**Chunk 1 (from reddit4.txt):** Learn how to master using libraries and APIs. Learn the cloud. Organizations will always have better computers or private programs that you could not make yourself in a million years.

**Chunk 2 (from reddit8.txt):** Just focus on one well-established language such as Java JavaScript Python or C# and become proficient at it. Learn algorithms data structures and design patterns.

**Chunk 3 (from reddit_6.txt):** Depends on how motivated you are to work on it. Most people of average intelligence are perfectly capable of completing a CS degree.

**Chunk 4 (from reddit10.txt):** Be good at Leetcode and you will get a job you can write a project in a day by following a youtube tutorial.

**Chunk 5 (from reddit9.txt):** Build stuff outside of class. Follow tutorials to build web sites mobile apps whatever interests you. Look up job postings that might interest you. See what they expect you to know.

---

## Retrieval Test Results

**Query 1:** What should CS students learn outside of class?
- Result 1 (reddit4.txt): Learn how to master using libraries and APIs. Learn the cloud...
- Result 2 (reddit8.txt): Just focus on one well-established language...
- Why relevant: Both chunks directly answer what to learn outside class matching the query semantically even without exact word overlap.

**Query 2:** How hard is it to finish a CS degree?
- Result 1 (reddit_6.txt): Depends on how motivated you are to work on it. Most people of average intelligence are perfectly capable...
- Result 2 (Reddit_5.txt): I did it in 2.5 years because I had a years worth of credits from high school...
- Why relevant: Both chunks address CS degree difficulty and completion directly.

**Query 3:** How do I build practical programming skills?
- Result 1 (reddit8.txt): Build a simple web app in React Node Express and PostgreSQL. Deploy to AWS and check the code into Git...
- Result 2 (reddit9.txt): Build stuff outside of class. Follow tutorials to build web sites mobile apps...
- Why relevant: Both chunks give concrete actionable advice on building real skills outside the classroom.

---

## Example Responses

**Example 1 — Grounded response:**
Query: What should I study to become a software developer?
Answer: According to the provided context to become a software developer you should study a programming language like Java JavaScript Python or C# and algorithms and data structures. Sources: reddit8.txt reddit_3.txt reddit1.txt

**Example 2 — Out of scope refusal:**
Query: What do CS students wish they knew earlier?
Answer: I dont have enough information on that. The provided context discusses what CS students should be learning outside the classroom but does not provide information on what they wish they knew earlier.
Sources: reddit9.txt Reddit_2.txt reddit4.txt

---

## Query Interface

**Input field:** A text box labeled Your question with placeholder text e.g. How do I prepare for a CS degree?

**Output fields:** Two text boxes. Answer showing the LLM response with inline citations and Sources listing the document filenames the answer was retrieved from.

**Sample interaction:**
- Input: How do I prepare before starting a CS degree?
- Answer: According to the post on r/learnprogramming to prepare for a CS degree you should refresh your math skills as CS degrees are math-heavy and review the requirements needed to graduate with a CS major.
- Sources: reddit1.txt reddit9.txt reddit_7.txt reddit_6.txt

---

## Evaluation Report

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | How do I prepare before starting a CS degree? | Study discrete math and practice coding early | Refresh math skills review graduation requirements with an advisor | Relevant | Accurate |
| 2 | What should CS students learn outside of class? | Build projects learn Git pursue internships | Master libraries and APIs learn cloud pick one language deeply | Relevant | Accurate |
| 3 | How hard is it to finish a CS degree? | Hard but doable with consistency | Depends on motivation most people of average intelligence can finish it | Relevant | Accurate |
| 4 | How do I build practical programming skills? | Build real projects contribute to open source | Pick one language build projects learn git and dev tools | Relevant | Accurate |
| 5 | What do CS students wish they knew earlier? | Start projects early network dont just study theory | System said it did not have enough information on that | Off-target | Inaccurate |

---

## Failure Case Analysis

**Question that failed:** What do CS students wish they knew earlier?

**What the system returned:** I dont have enough information on that. The provided context discusses what CS students should be learning outside the classroom and how much they struggled in their CS undergrad but it does not provide information on what they wish they knew earlier.

**Root cause (tied to a specific pipeline stage):** This is a vocabulary mismatch failure at the retrieval stage. None of the 10 documents used the phrase wish they knew earlier or similar regret-framing language. The retrieval pulled chunks about struggling in CS and learning outside class but no chunk directly addressed hindsight advice. Because the retrieved chunks were not semantically close enough to the query Groq correctly declined to generate an answer rather than hallucinate.

**What you would change to fix it:** Add 2-3 Reddit threads specifically about CS regrets or hindsight advice such as what I wish I knew as a CS freshman. This would give the retrieval system vocabulary that matches this type of question.

---

## Spec Reflection

**One way the spec helped you during implementation:** Writing the chunking strategy in planning.md before writing any code forced me to think about the structure of Reddit comments specifically. Because I decided on 500 characters and 50 character overlap before implementing anything I had a clear target when building chunk_text() instead of guessing. It also made prompting Claude for code much easier since I could paste the spec section directly.

**One way your implementation diverged from the spec, and why:** The evaluation questions in my final system differed from the ones in planning.md. The original planning questions were too vague so I replaced them with more specific ones that were easier to judge as accurate or inaccurate.

---

## AI Usage

**Instance 1**
- What I gave the AI: My Documents section with 10 Reddit URLs and Chunking Strategy section with 500 char chunks and 50 char overlap from planning.md
- What it produced: The ingest.py script with load_documents clean_text and chunk_text functions
- What I changed or overrode: I verified the output by printing 5 sample chunks and checking they looked like complete readable comments and confirmed the total chunk count was above 50.

**Instance 2**
- What I gave the AI: My Retrieval Approach section and pipeline architecture diagram from planning.md
- What it produced: The embed.py script that embeds chunks using all-MiniLM-L6-v2 and stores them in ChromaDB with source metadata plus a retrieval test function
- What I changed or overrode: I tested retrieval with 3 of my evaluation questions and manually checked that the returned chunks were relevant to each question before moving to the generation step.

---

## Demo Video
https://www.youtube.com/watch?v=sw9OjuCG1vs
