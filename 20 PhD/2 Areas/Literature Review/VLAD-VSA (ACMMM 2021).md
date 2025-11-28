aliases: [vlad_vsa_fas]
tags: [paper, pad, deep-fas-survey, domain-generalization]
authors: Jiong Wang, Zhou Zhao, Weike Jin, Xinyu Duan, Zhen Lei, Baoxing Huai, Yiling Wu, Xiaofei He
year: 2021
venue: ACM MM 2021
paper_url: https://dl.acm.org/doi/abs/10.1145/3474085.3475284
code_url: https://github.com/Liubinggunzu/VLAD-VSA
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
## What does the paper present?
**Abstract:** For face presentation attack detection (PAD), most of the spoofing cues are subtle, local image patterns (e.g., local image distortion, 3D mask edge and cut photo edges). The representations of existing PAD works with simple global pooling method, however, lose the local feature discriminability. In this paper, the VLAD aggregation method is adopted to quantize local features with visual vocabulary locally partitioning the feature space, and hence preserve the local discriminability. We further propose the vocabulary separation and adaptation method to modify VLAD for cross-domain PAD task. The proposed vocabulary separation method divides vocabulary into domain-shared and domain-specific visual words to cope with the diversity of live and attack faces under the cross-domain scenario. The proposed vocabulary adaptation method imitates the maximization step of the k-means algorithm in the end-to-end training, which guarantees the visual words be close to the center of assigned local features and thus brings robust similarity measurement.

**Method:** VLAD-VSA

## What are my views on it?
