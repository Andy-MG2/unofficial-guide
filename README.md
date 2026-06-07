# The Unofficial Guide  NJIT BME Professor Reviews

---

## Domain

This system covers student reviews of Biomedical Engineering (BME) professors at New Jersey Institute of Technology (NJIT), sourced from Rate My Professors and the r/NJTech subreddit. This knowledge is valuable because official university channels, course catalogs, department websites, and faculty pages — describe what professors research, not how they teach. A student trying to decide between professors for BME 304 has no official way to learn that one professor's exams are disconnected from lecture material, or that another genuinely goes out of their way to help struggling students. Rate My Professors reviews and Reddit threads fill that gap with first-hand student experience that is otherwise scattered and hard to search.

---

## Document Sources

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | Rate My Professors — Bryan Pfister | RMP reviews | https://www.ratemyprofessors.com/professor/952505 |
| 2 | Rate My Professors — Amir Miri | RMP reviews | https://www.ratemyprofessors.com/professor/2745962 |
| 3 | Rate My Professors — Mesut Sahin | RMP reviews | https://www.ratemyprofessors.com/professor/799947 |
| 4 | Rate My Professors — Tara Alvarez | RMP reviews | https://www.ratemyprofessors.com/professor/186910 |
| 5 | Rate My Professors — Bharat Biswal | RMP reviews | https://www.ratemyprofessors.com/professor/1986630 |
| 6 | Rate My Professors — Sergei Adamovich | RMP reviews | https://www.ratemyprofessors.com/professor/404160 |
| 7 | Rate My Professors — Eun Jung Lee | RMP reviews | https://www.ratemyprofessors.com/professor/1696813 |
| 8 | Rate My Professors — Jongsang Son | RMP reviews | https://www.ratemyprofessors.com/professor/2833328 |
| 9 | Rate My Professors — Vivek Kumar | RMP reviews | https://www.ratemyprofessors.com/professor/2341169 |
| 10 | Rate My Professors — Treena Arinzeh | RMP reviews | https://www.ratemyprofessors.com/professor/212358 |
| 11 | Rate My Professors — Joel Schesser | RMP reviews | https://www.ratemyprofessors.com/professor/1933579 |
| 12 | Reddit r/NJTech — General BME discussion | Reddit thread | https://www.reddit.com/r/NJTech/comments/zuq7xj/biomedical_engg/ |
| 13 | Reddit r/NJTech — BME 303 discussion | Reddit thread | https://www.reddit.com/r/NJTech/comments/1ibifdu/bme_303/ |
| 14 | Reddit r/NJTech — BME 301 discussion | Reddit thread | https://www.reddit.com/r/NJTech/comments/aetaao/bme301/ |
| 15 | Reddit r/NJTech — Tips for BME 303 with Haorah | Reddit thread | https://www.reddit.com/r/NJTech/comments/l1be46/tips_for_bme_303_w_haorah/ |
| 16 | Reddit r/NJTech — Is there any hope BME 301 | Reddit thread | https://www.reddit.com/r/NJTech/comments/bghlgu/is_there_any_hope_bme_301/ |
| 17 | Reddit r/NJTech — Which BME track should I choose | Reddit thread | https://www.reddit.com/r/NJTech/comments/13e9tx8/which_bme_track_should_i_choose_and_why/ |
| 18 | Reddit r/NJTech — BME 302 discussion | Reddit thread | https://www.reddit.com/r/NJTech/comments/1ojsc6o/bme_302/ |

---

## Chunking Strategy

**Chunk size:** One review per chunk. Each `---` separated block in the .txt files is treated as a single chunk regardless of character length. The minimum chunk size observed is approximately 160 characters (a full metadata header plus a one-sentence review).

**Overlap:** None. Overlap is unnecessary because each review is written independently by a different student. There is no shared context across review boundaries  each chunk is a completely standalone opinion.

**Why these choices fit the documents:** RMP reviews are pre-chunked, each review already contains everything needed to answer a query: the professor name, course number, quality and difficulty scores, tags, and the student's written opinion. Forcing a fixed character split would split reviews mid-sentence and destroy the semantic of each opinion. Keeping one review per chunk also ensures that when a user asks about a specific professor or course, the retrieved chunks each represent a complete student perspective not a fragment.

Each chunk is structured with metadata prepended (professor name, course, quality rating, difficulty rating, would take again, tags) to give the embedding model additional signal for queries about ratings and difficulty that the review text alone might not answer.

**Final chunk count:** 142 chunks across 11 professor files.

**Sample chunks:**

**Chunk 1**  `alvarez_tara_rmp.txt`
```
Professor: Tara Alvarez
Course: BME472
Date: Sep 23rd, 2023
Quality: 5.0
Difficulty: 3.0
Would Take Again: Yes
Grade: A
Tags: N/A
Review: Excellent Teacher. Course material is dry but what do you expect about an FDA regulatory class. Most important class that got me my job.
```

**Chunk 2**  `son_jongsang_rmp.txt`
```
Professor: Jongsang Son
Course: BME451
Date: Oct 21st, 2022
Quality: 5.0
Difficulty: 3.0
Would Take Again: Yes
Grade: Not sure yet
Tags: Amazing lectures, Inspirational, Respected
Review: It is not an exaggeration to say that Dr. Son is the best professor I have had in my 4.5 years at NJIT. He truly cares about each of his students, and makes sure everyone understands his lectures.
```

**Chunk 3**  `sahin_mesut_rmp.txt`
```
Professor: Mesut Sahin
Course: BME301
Date: Dec 30th, 2023
Quality: 1.0
Difficulty: 5.0
Would Take Again: N/A
Grade: D
Tags: Tough grader, Lecture heavy, Test heavy
Review: Escape from him if you want to pass this class.
```

**Chunk 4** - `biswal_bharat_rmp.txt`
```
Professor: Bharat Biswal
Course: BME471
Date: Dec 23rd, 2020
Quality: 4.0
Difficulty: 2.0
Would Take Again: Yes
Grade: A
Tags: Respected, Lecture heavy, Extra Credit
Review: He's an easy A professor. I feel comfortable asking him questions because I know that he knows the answer. It was an easy and enjoyable class.
```

**Chunk 5** - `lee_eunjung_rmp.txt`
```
Professor: Eun Jung Lee
Course: BME302
Date: May 1st, 2012
Quality: 1.0
Difficulty: 5.0
Would Take Again: N/A
Tags: N/A
Review: She does not cover the material on the assignments, quizzes, tests, or labs. She does not answer questions or solve out problems completely. The class average was in the 50s and no one knew what was going on.
```

---

## Embedding Model

**Model used:** `all-MiniLM-L6-v2` via `sentence-transformers`. This model runs locally with no API key and no rate limits. It produces 384-dimensional embeddings and has a 256-token context window. It is well-suited for short opinion-based text like RMP reviews, where each chunk is a self-contained paragraph or less.

**Production tradeoff reflection:** For a production deployment I would consider switching to OpenAI's `text-embedding-3-small` for higher accuracy at low cost, or Cohere's `embed-english-v3.0` which is optimized specifically for retrieval tasks. The main tradeoffs would be latency which we see in API network round-trip , cost per-token , and context length. `all-MiniLM-L6-v2` caps at 256 tokens which is sufficient for short RMP reviews but would be a problem if the corpus included longer documents like syllabi or handbooks. Multilingual support is not a needed here since all reviews are in English. For a system serving thousands of users, the API-based models would likely be worth the cost for improved semantic accuracy, especially on ambiguous queries.

---

## Retrieval Test Results

**Query 1:** "Is Bryan Pfister a laid back professor?"

Top returned chunks:
Pfister Bryan (distance: 0.4641)

Professor: Bryan Pfister
Course: BME420
Date: Jan 26th, 2009
Quality: 5.0
Difficulty: 2.0
Would Take Again: N/A
Textbook: No
Tags: N/A
Helpful: 0 | Not Helpful: 5
Review: Very easy professor if you go to class and take notes. All his exams are from his notes and is a really fair guy. He gives projects and hw to boost everyones grade.
Pfister Bryan (distance: 0.5109)

Professor: Bryan Pfister
Course: BME420
Date: Jul 24th, 2012
Quality: 3.0
Difficulty: 3.0
Would Take Again: N/A
Textbook: No
Tags: N/A
Helpful: 5 | Not Helpful: 2
Review: Homework was impossible. He put things on the exam when he said he wouldn't and made mistakes while teaching on the board.
Pfister Bryan (distance: 0.5779)

Professor: Bryan Pfister
Course: BME420
Date: Apr 6th, 2008
Quality: 3.0
Difficulty: 2.0
Would Take Again: N/A
Textbook: Yes
Tags: N/A
Helpful: 5 | Not Helpful: 0
Review: No Comments
Miri Amir (distance: 0.5900)

Professor: Amir Miri
Course: BME680
Date: Jul 26th, 2023
Quality: 1.0
Difficulty: 5.0
Would Take Again: N/A
Grade: Rather not say
Attendance: Mandatory
Textbook: Yes
Tags: Tough grader, Lots of homework, Beware of pop quizzes
Helpful: 0 | Not Helpful: 1
Review: If you don't care, don't act like you do. He acts like he does just because he knows every student's name, which ain't hard when enrollment in his classes is low. Can't teach for nothing. Dude multiple times implied he would not let me graduate, both privately and in front of the class, and not in a jocular way. Worst. Prof. Ever.
Son Jongsang (distance: 0.6178)

Professor: Jongsang Son
Course: BME451
Date: Oct 21st, 2022
Quality: 5.0
Difficulty: 3.0
Would Take Again: Yes
Grade: Not sure yet
Attendance: Mandatory
Textbook: Yes
Tags: Amazing lectures, Inspirational, Respected
Helpful: 0 | Not Helpful: 0
Review: It is not an exaggeration to say that Dr. Son is the best professor I have had in my 4.5 years at NJIT. He truly cares about each of his students, and makes sure everyone understands his lectures. Seriously, in nearly 5 years at this school, this is the first professor I've felt truly cared about our success. This class is very interesting as well.


*Why these chunks are relevant:* The query asks specifically about Pfister by name, and the professor name is embedded in every chunk header, so retrieval correctly surfaces all of his reviews. The top result directly addresses teaching style, difficulty, and style of teaching 

---

**Query 2:** "What do students say about Amir Miri's BME 680 course?"

Top returned chunks:'

Miri Amir (distance: 0.2436)

Professor: Amir Miri
Course: BME680
Date: Sep 4th, 2023
Quality: 5.0
Difficulty: 3.0
Would Take Again: Yes
Grade: A
Attendance: Mandatory
Textbook: Yes
Tags: Participation matters, Group projects, Accessible outside class
Helpful: 2 | Not Helpful: 0
Review: The class had a large project with details for a tough course like BME 680. If you do well in the class, you have an easy job to do the project and then get a good grade. The learning comes with the project, even if it takes time.
Miri Amir (distance: 0.2483)

Professor: Amir Miri
Course: BME680
Date: Sep 6th, 2023
Quality: 4.0
Difficulty: 3.0
Would Take Again: Yes
Grade: Rather not say
Attendance: Mandatory
Textbook: Yes
Tags: Group projects, Amazing lectures, Respected
Helpful: 2 | Not Helpful: 0
Review: The course material is explanatory. Despite being quite hard, the project component teaches a lot of the course material and program. As a graduate student, you must study certain things on your own in this course. The professor tried to connect the lectures to ongoing research projects and the challenges in implementing new practicals.
Miri Amir (distance: 0.2959)

Professor: Amir Miri
Course: BME451
Date: Sep 24th, 2022
Quality: 5.0
Difficulty: 3.0
Would Take Again: Yes
Grade: A
Attendance: Mandatory
Textbook: Yes
Tags: Extra Credit, Gives good feedback, Inspirational
Helpful: 2 | Not Helpful: 1
Review: Good experience compared to the rest of the college. The main thing is to have someone listen to students.
Miri Amir (distance: 0.2968)

Professor: Amir Miri
Course: BME680
Date: Jan 1st, 2026
Quality: 5.0
Difficulty: 3.0
Would Take Again: Yes
Grade: A
Attendance: Mandatory
Textbook: Yes
Tags: Amazing lectures, Inspirational, Respected
Helpful: 0 | Not Helpful: 0
Review: Good work done by the teacher for the class and heavy engagement of all students.
Miri Amir (distance: 0.3054)

Professor: Amir Miri
Course: BME680
Date: Jun 9th, 2024
Quality: 1.0
Difficulty: 5.0
Would Take Again: N/A
Grade: C
Attendance: N/A
Textbook: N/A
Tags: Tough grader, Participation matters, Lots of homework
Helpful: 0 | Not Helpful: 0
Review: You work and work, but its for no avail. BME 680 is not intended for students who aren't pursuing PhD's. The prof makes no effort to help out students, and only shines the light on the PhD's who are pursuing projects already similar to the course material. At that point, the course has no value for anyone besides him and his punitive standards.


*Why these chunks are relevant:* The query names both the professor and the specific course number. The embedding correctly anchors on "Amir Miri" and "BME 680" appearing together in the chunk text, surfacing a mix of positive and negative BME 680 reviews.

---

**Query 3:** "Which BME professor cares most about their students?"

Lee Eunjung (distance: 0.4266)

Professor: Eun Jung Lee
Course: BME385
Date: Oct 4th, 2023
Quality: 1.0
Difficulty: 5.0
Would Take Again: N/A
Grade: B+
Attendance: Mandatory
Textbook: N/A
Tags: Tough grader, Lots of homework
Helpful: 0 | Not Helpful: 0
Review: She's tenured, so expect the least from her. Barely provides useful information. Grades labs and tests randomly. The fact that anyone lets her teach this course shows the laziness of the BME department.
Kumar Vivek (distance: 0.4460)

Professor: Vivek Kumar
Course: BME420
Date: May 7th, 2021
Quality: 1.0
Difficulty: 5.0
Would Take Again: No
Grade: A
Attendance: Mandatory
Textbook: Yes
Tags: Lots of homework, Skip class you won't pass, Group projects
Helpful: 0 | Not Helpful: 0
Review: Worst BME teacher ever.
Miri Amir (distance: 0.4563)

Professor: Amir Miri
Course: BME680
Date: Jun 9th, 2024
Quality: 1.0
Difficulty: 5.0
Would Take Again: N/A
Grade: C
Attendance: N/A
Textbook: N/A
Tags: Tough grader, Participation matters, Lots of homework
Helpful: 0 | Not Helpful: 0
Review: You work and work, but its for no avail. BME 680 is not intended for students who aren't pursuing PhD's. The prof makes no effort to help out students, and only shines the light on the PhD's who are pursuing projects already similar to the course material. At that point, the course has no value for anyone besides him and his punitive standards.
Sahin Mesut (distance: 0.4658)

Professor: Mesut Sahin
Course: BME386
Date: Dec 25th, 2022
Quality: 1.0
Difficulty: 3.0
Would Take Again: N/A
Grade: B+
Attendance: Mandatory
Textbook: N/A
Tags: Tough grader
Helpful: 0 | Not Helpful: 0
Review: He grades you against other students in the class. I was extremely unlucky this semester to be with the smartest students in the whole BME track and even with the highest scores on lab grades, above average on exams, he still gave me a B+, which I would never get if I was stuck in a class with more variability in performance.
Lee Eunjung (distance: 0.4735)

Professor: Eun Jung Lee
Course: BME302
Date: Sep 17th, 2012
Quality: 2.0
Difficulty: 4.0
Would Take Again: N/A
Grade: N/A
Attendance: N/A
Textbook: No
Tags: N/A
Helpful: 6 | Not Helpful: 0
Review: Hands down one of the most useless professors in NJIT. She doesn't answer questions clearly and expects us to know stuff she never taught. Her assignments are nothing like her lectures. Brings no energy to class.


Top returned chunks included reviews from Son Jongsang, Eunjung Lee, and Kumar Vivek with distances ranging from 0.42 to 0.49. Interestingly enough all reviews were negative. I could not figure out why.

---

## Grounded Generation

**System prompt grounding instruction:**

```
You are an assistant that helps NJIT students choose BME professors.
Answer the user's question using ONLY the student reviews provided below.
Do not use any outside knowledge or make assumptions beyond what the reviews say.
Always cite which professor the information comes from.
If the reviews do not contain enough information to answer the question,
say exactly: 'I don't have enough information in the reviews to answer that.'
```

**How source attribution is surfaced in the response:** Source attribution is handled after generation, the system collects the unique professor names from all retrieved chunks and displays them as a bulleted "Sources" list in the Streamlit UI, separate from the LLM's answer. The LLM is also instructed to cite the professor's name inline in its answer. This means attribution is guaranteed by the pipeline structure, not left to the model.

---

## Example System Responses

**Response 1 - Grounded answer with citation:**

Query: *"What do students say about Amir Miri's BME 680 course?"*

According to the reviews from students, here's what they say about Amir Miri's BME 680 course:

One student (Sep 6th, 2023 review) says the course material is explanatory, and the project component teaches a lot, but as a graduate student, you must study certain things on your own. The same student praises the professor for trying to connect lectures to ongoing research projects.

Another student (Sep 4th, 2023 review) mentions that the class had a large project, and if you do well in the class, you have an easy job to do the project and then get a good grade. This student also notes that the learning comes with the project, even if it takes time.

However, a different student (Jun 9th, 2024 review) had a negative experience, stating that the course is not intended for students who aren't pursuing PhD's, and the professor only shines the light on PhD students. This student also mentions that the professor makes no effort to help out students and has punitive standards.

On the other hand, another student (Jan 1st, 2026 review) praises the teacher for good work done in the class and heavy engagement of all students, calling the lectures "amazing" and the professor "inspirational" and "respected".

It's worth noting that the reviews are inconsistent, with some students having a very positive experience (Sep 6th, 2023, Sep 4th, 2023, and Jan 1st, 2026 reviews) and one student having a very negative experience (Jun 9th, 2024 review).

Sources: Miri Amir

---

**Response 2 - Grounded answer with citation:**

Query: *"Is Bryan Pfister an easy professor?"*

> According to the reviews from Pfister Bryan, the answer to whether Bryan Pfister is an easy professor is mixed. One review (Jan 26th, 2009) states that he is "Very easy professor if you go to class and take notes" with a difficulty rating of 2.0. However, another review (Jul 24th, 2012) states that "Homework was impossible" with a difficulty rating of 3.0, and a third review (Apr 6th, 2008) gives a difficulty rating of 2.0 but has no comments. Therefore, it seems that Bryan Pfister's ease of teaching may vary depending on the student's experience.

Sources:  
- Alvarez Tara
- Pfister Bryan
- Miri Amir

---

**Out-of-scope refusal response:**

Query: *"What are the best restaurants near NJIT?"*

> I don't have enough information in the reviews to answer that.

Sources: 
- Kumar Vivek

- Lee Eunjung

- Alvarez Tara

- Son Jongsang

---

## Evaluation Report

| # | Question | Expected Answer | System Response (summarized) | Retrieval Quality | Response Accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | Is Bryan Pfister a laid back professor? | Yes - goes to class and takes notes, exams are directly from notes, fair grader | Correctly summarized Pfister as generally easy and fair, noted one negative review about unexpected exam content | Relevant | Accurate |
| 2 | I'm looking for a BME 301 professor that teaches well and difficulty isn't an obstacle | Pfister Bryan, Miri Amir, Alvarez Tara | I don't have enough information in the reviews to answer that. | Refused | Not good |
| 3 | What do students say about Amir Miri's BME 680 course? | Divided positive reviews praise project work, negative reviews cite humiliation and syllabus changes | System returned a balanced summary citing both positive and negative reviews with professor attribution | Relevant | Accurate |
| 4 | Which NJIT BME professor is most recommended for caring about students? | Jongsang Son - consistently praised for caring about every student | System returned mixed results including negative reviews about professors who don't care - failed to surface Son as the clear answer | Partially relevant | Inaccurate |
| 5 | What do students say about Eun Jung Lee's exams? | Exams are random, disconnected from lecture material, class averages in the 50s | System correctly returned Lee's reviews describing exams as unrelated to lecture content, class averages failing | Relevant | Accurate |

---

## Failure Case Analysis

**Question that failed:** "Which NJIT BME professor is most recommended for caring about students?"

**What the system returned:** Reviews from Biswal, Kumar, and Lee, some negative reviews mentioning students in a negative context  rather than Son Jongsang's reviews which are the clearest positive answer in the corpus.

**Root cause (tied to a specific pipeline stage):** This is a retrieval failure caused by a fundamental limitation of the embedding model at the retrieval stage. The `all-MiniLM-L6-v2` model encodes semantic similarity based on word co-occurrence patterns, but has no way of understanding negation. The query "caring about students" produces an embedding vector that is mathematically close to chunks containing "doesn't care about students" or "does not care about the students" because the high-signal words (care, students) are identical. Son Jongsang's reviews use different vocabulary  "sweetest guy", "best professor I've had", "truly cares about teaching", which doesn't align as closely with the query wording as the negated versions do. There also arent enough reviews/ data to get a general consensus.

**What I would change to fix it:** A hybrid search approach combining semantic search with sentiment filtering would address this. Running a lightweight sentiment classifier on retrieved chunks before passing them to the LLM would filter out negative results for positive queries. Hving more review data and being able to pull and process a lot more chunks to get a general consensus would be the largest improvement by far

---

## Query Interface

The interface is built with Streamlit and runs at `http://localhost:8501` via `streamlit run app.py`.

**Input fields:**
- Text input labeled "Ask a question about a BME professor or course" — accepts any natural language question

**Output fields:**
- **Answer** — the LLM-generated response grounded in retrieved reviews, with inline professor citations
- **Sources** — a bulleted list of professor names whose reviews were retrieved and passed to the LLM

**Sample interaction transcript:**

```
User: What do students say about Jongsang Son?

Answer:
According to the reviews from Son Jongsang, students say that Jongsang Son is "truly a great professor and actually cares about teaching" (May 3rd, 2023 review), "the best professor I have had in my 4.5 years at NJIT" who "truly cares about each of his students, and makes sure everyone understands his lectures" (Oct 21st, 2022 review). They also mention that he gives "amazing lectures" (May 3rd, 2023 and Oct 21st, 2022 reviews) and is "inspirational" (Oct 21st, 2022 review). However, some students also mention that he is a "tough grader" with "lots of homework" (Apr 23rd, 2024 review) and that it's "not easy to be prepared for the exam" (Apr 23rd, 2024 review). One review also states that he is "not communicative" (Jun 11th, 2024 review).

Sources:
- Son Jongsang
- Lee Eunjung
```

---

## Spec Reflection

**One way the spec helped during implementation:** The requirement to write `planning.md` before any code forced me to decide on the chunking strategy  one review per chunk split on `---` separators,before touching the pipeline. This decision turned out to be right for the data structure. Having the chunk format specified in advance also made it straightforward to prompt Claude to generate the ingestion code that matched the exact format.

**One way implementation diverged from the spec:** The spec and planning.md specified a similarity threshold of 0.6 for filtering retrieved chunks. During testing this threshold was too aggressive  many relevant chunks were being filtered out before reaching the LLM, causing the system to return "I don't have enough information" even when relevant reviews existed in the vector store. The threshold was raised to 0.9 and eventually removed entirely from some query paths. This divergence happened because cosine distances on short review-style text tend to run higher than on longer documents, which was not anticipated in the planning phase.

---

## AI Usage

**Instance 1**

- *What I gave the AI:* My chunking strategy section from planning.md, the format of the `.txt` files showing the `---` separator between reviews, and the chunk dictionary structure I wanted (`review`, `professor`, `chunk_id`).
- *What it produced:* A `chunk_document()` function that split on `\n---\n` and returned a list of chunk dictionaries.
- *What I changed or overrode:* The initial version stored `reviews` (the whole list) instead of `review` (the current string) as the key  a variable name bug that caused ChromaDB to reject the chunks. I identified and fixed this manually by reading the error output. I also removed the `[1:]` slice initially suggested to skip the header chunk, then added it back after realizing the header block was being embedded unnecessarily.

**Instance 2**

- *What I gave the AI:* My retrieval approach section from planning.md, the chunk format from Milestone 3, and the requirement that responses be grounded with source attribution.
- *What it produced:* The full `generator.py` with a Groq client, system prompt enforcing grounding, context block formatted from retrieved chunks, and source list extracted programmatically.
- *What I changed or overrode:* The initial system prompt said "if the reviews do not contain enough information, say so"  I tightened this to an exact phrase ("say exactly: 'I don't have enough information in the reviews to answer that.'") so the refusal response would be consistent and testable. I also added a try/except block after discovering a silent Groq API error.
