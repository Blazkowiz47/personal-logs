# TODO: Integrate DeepFAS Survey into Obsidian Vault

This plan outlines the steps to deconstruct the `DeepFAS` survey repository and integrate its contents into the `20 PhD` section of the Obsidian vault.

- [ ] **1. Preparation & Parsing**
    - [ ] Read and parse `DeepFAS/README.md` to extract tables for datasets and papers.
    - [ ] Read the paper template from `Templates/Paper Note Template.md` to use for new notes.

- [ ] **2. Asset Migration**
    - [ ] Create a directory `20 PhD/3 Resources/Attachments` for images and other assets if it does not exist.
    - [ ] Move `DeepFAS/Topology.png` to `20 PhD/3 Resources/Attachments/DeepFAS-Topology.png`.

- [ ] **3. Dataset Note Integration**
    - [ ] For each dataset in the parsed tables, find the corresponding note in `20 PhD/2 Areas/Dataset Management (OCIM)/`.
    - [ ] Update each dataset note with the information (Year, Size, Attack Types, etc.) from the survey.
    - [ ] Create new dataset notes if they don't exist for entries in the survey.

- [ ] **4. Paper Note Creation**
    - [ ] For each paper identified in the `Deep FAS methods` tables:
        - [ ] Create a new file in `20 PhD/2 Areas/Literature Review/`.
        - [ ] Name the file based on the paper's title/method (e.g., `DPCNN - 2016.md`).
        - [ ] Populate the file's frontmatter and body with information from the table (Year, Backbone, Loss, etc.), following the `Paper Note Template.md`.
        - [ ] Add a tag for the paper's category (e.g., `#hybrid-method`, `#zero-shot-learning`).

- [ ] **5. Create Central Index**
    - [ ] Create a new file: `20 PhD/2 Areas/Literature Review/DeepFAS Survey Index.md`.
    - [ ] In this file, recreate the structure of the original `DeepFAS/README.md` (e.g., "Hybrid methods", "Domain Generalization").
    - [ ] Under each heading, add links to the newly created paper notes.
    - [ ] Add links to the updated dataset notes.
    - [ ] Embed the `DeepFAS-Topology.png` image from its new location.

- [ ] **6. Final Cleanup**
    - [ ] Review all created and updated files for correctness.
    - [ ] Ask for user confirmation to delete the `DeepFAS` directory.
    - [ ] Upon completion of all tasks, delete this `TODO.md` file.
