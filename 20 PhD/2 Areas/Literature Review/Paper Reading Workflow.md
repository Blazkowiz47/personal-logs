# 📖 Paper Reading Workflow Guide

This guide explains how to effectively use the paper tracking system in your Obsidian vault.

## Quick Start

### 1. Adding a New Paper
1. Go to `Templates/Paper Note Template.md`
2. Use Templater (or copy the template)
3. Create new note in `20 PhD/2 Areas/Literature Review/`
4. Name it with the paper title
5. Fill in the frontmatter metadata:
   ```yaml
   tags: [paper, pad]  # Add relevant topic tags
   authors: First Author et al.
   year: 2024
   venue: CVPR 2024
   paper_url: https://...
   code_url: https://...
   status: "📚 To Read"
   dateadded: 2025-10-18
   priority: medium
   ```

### 2. Topic Tags to Use
Add relevant tags to help organize papers:
- `#pad` - Presentation Attack Detection
- `#mad` - Morph Attack Detection  
- `#deepfake` - DeepFake Detection
- `#multimodal` - Multi-modal approaches
- `#cross-modal` - Cross-modal learning
- `#domain-adaptation` - Domain adaptation/generalization
- `#benchmark` - Benchmark papers
- `#survey` - Survey/review papers
- `#dataset` - Papers introducing datasets
- `#to-implement` - Papers you want to implement
- `#high-priority` - High priority reading

### 3. Status Values
Update the `status` field as you read:
- `📚 To Read` - In your reading queue
- `📖 Reading` - Currently reading
- `✅ Read` - Finished and summarized

### 4. Reading a Paper

#### Active Reading Process
1. **First Pass (Quick Scan)** - 5-10 minutes
   - [ ] Read title, abstract, figures
   - [ ] Fill in Quick Summary section
   - [ ] Note key contributions
   
2. **Second Pass (Detailed Read)** - 30-60 minutes
   - [ ] Read introduction and conclusion
   - [ ] Understand methodology
   - [ ] Fill in Problem Statement, Methodology sections
   - [ ] Note strengths and limitations
   
3. **Third Pass (Deep Dive)** - 1-2 hours
   - [ ] Read everything including supplementary
   - [ ] Complete all sections
   - [ ] Add critical analysis
   - [ ] Link related papers
   - [ ] Note implementation details
   
4. **Post-Reading**
   - Update status to `✅ Read`
   - Add `dateread` in frontmatter
   - Update [[Papers Database]]

### 5. Taking Notes

#### Use the Structured Sections
- **Quick Summary** - One sentence (for quick reference)
- **Problem Statement** - What gap does it fill?
- **Key Contributions** - List 3-5 main contributions
- **Methodology** - Architecture, techniques, novel components
- **Experiments** - Datasets, results, ablations
- **Critical Analysis** - Your thoughts (most important!)
- **Relevance to My Work** - How it relates to your research

#### Capture Important Details
- Add key quotes with `>`
- Note figure numbers that are useful
- Copy important equations using LaTeX
- Highlight novel techniques

### 6. Linking Papers
Create connections between papers:
```markdown
## Related Papers
### Cited By This Paper
- [[ArcFace]] - Uses similar margin-based loss
- [[MagFace]] - Extends the approach

### Papers That Cite This  
- [[Paper X]] - Applies to PAD

### Similar Approaches
- [[Paper Y]] - Different architecture, same problem
```

### 7. Using the Papers Database

Access via: `20 PhD/2 Areas/Literature Review/Papers Database.md`

The database automatically organizes papers by:
- Status (To Read, Reading, Read)
- Topic (PAD, MAD, DeepFake, etc.)
- Venue (CVPR, ICCV, journals)
- Year
- Priority
- Implementation status

#### Useful Views:
- **Recently Added** - See what you've added recently
- **Papers with Code** - Find reproducible papers
- **To Implement** - Papers marked for implementation
- **High Priority** - Papers marked urgent

### 8. Best Practices

#### Daily Routine
- [ ] Check Papers Database for to-read queue
- [ ] Read 1-2 papers per day (depending on complexity)
- [ ] Update status as you progress
- [ ] Link to related papers in your vault

#### Weekly Review
- [ ] Review papers read this week
- [ ] Update Literature Review Index with key themes
- [ ] Identify research gaps
- [ ] Plan next week's reading

#### Monthly Review
- [ ] Analyze reading patterns
- [ ] Update research directions based on literature
- [ ] Clean up and reorganize if needed
- [ ] Archive less relevant papers

### 9. Integration with Research

#### Link Papers to Projects
```markdown
In your project notes:
This project builds on [[Paper Name]] by extending...
```

#### Extract Implementation Details
Use the Implementation Notes section to capture:
- Hyperparameters
- Architecture details
- Training tricks
- Reproducibility notes

#### Track Experimental Ideas
Use the "Questions & Future Directions" section to:
- Note extension ideas
- Track open questions
- Plan experiments

### 10. Search & Discovery

#### Finding Papers
Use Obsidian's search with tags:
- `tag:#pad tag:#high-priority` - High priority PAD papers
- `tag:#to-implement` - Implementation candidates
- `tag:#benchmark` - Benchmark papers

#### Dataview Queries
The Papers Database uses Dataview for dynamic views. You can create custom queries in any note:

```dataview
TABLE authors, year, venue
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "pad") AND year >= 2023
SORT year DESC
```

## Common Workflows

### Workflow 1: Conference Paper Sprint
When a major conference publishes proceedings:
1. Create notes for all relevant papers with basic metadata
2. Mark high-priority ones with `#high-priority` tag
3. Set status as `📚 To Read`
4. Read and summarize high-priority papers first
5. Update status as you complete each

### Workflow 2: Deep Dive on Topic
When researching a specific topic:
1. Search Papers Database by topic tag
2. Create a new project note that links key papers
3. Read papers in chronological order
4. Track evolution of ideas across papers
5. Identify research gaps and opportunities

### Workflow 3: Implementation Planning
When planning to implement a paper:
1. Read paper thoroughly
2. Add `#to-implement` tag
3. Fill Implementation Notes section completely
4. Link to related code repositories
5. Create experiment tracking note in PhD project

### Workflow 4: Writing Related Work
When writing related work for a paper:
1. Use Papers Database to filter by topic
2. Sort by year to show progression
3. Extract key contributions from each paper
4. Link papers that build on each other
5. Identify your work's unique position

## Tips & Tricks

1. **Use Aliases** - Add paper abbreviations as aliases
   ```yaml
   aliases: [FMF, Flexible Modal Face]
   ```

2. **Create Reading Lists** - Make note collections for specific purposes
   ```markdown
   # Papers for Literature Review Section
   - [[Paper 1]]
   - [[Paper 2]]
   ```

3. **Visual Connections** - Use graph view to see paper relationships

4. **Quick Capture** - Keep a "Papers to Add" note for quick captures during meetings

5. **Review Schedule** - Use periodic notes to schedule regular paper reading

---

## Quick Reference Card

| Action | Steps |
|--------|-------|
| Add paper | Template → Fill metadata → Save in Literature Review folder |
| Update status | Edit frontmatter `status` field |
| Link papers | Use `[[Paper Name]]` in Related Papers section |
| Find papers | Use Papers Database or search by tags |
| Mark priority | Add `#high-priority` tag |
| Track implementation | Add `#to-implement` tag |
| Review reading | Check Papers Database weekly view |

---

**Remember:** The goal is to build a interconnected knowledge base that helps you:
- Track what you've read
- Remember key insights
- Connect ideas across papers  
- Identify research opportunities
- Support your PhD research

Start simple, and gradually add more detail as you develop your system!
