aliases: [oneclasskd_fas]
tags: [paper, pad, deep-fas-survey, anomaly-detection]
authors: Zhi Li, Rizhao Cai, Haoliang Li, Kwok-Yan Lam, Yongjian Hu, Alex C. Kot
year: 2022
venue: IEEE Transactions on Information Forensics and Security (TIFS)
paper_url: https://arxiv.org/abs/2205.03792
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
# One-Class Knowledge Distillation for Face Presentation Attack Detection

> [!abstract]
> Face presentation attack detection (PAD) has been extensively studied by research communities to enhance the security of face recognition systems. Although existing methods have achieved good performance on testing data with similar distribution as the training data, their performance degrades severely in application scenarios with data of unseen distributions. In situations where the training and testing data are drawn from different domains, a typical approach is to apply domain adaptation techniques to improve face PAD performance with the help of target domain data. However, it has always been a non-trivial challenge to collect sufficient data samples in the target domain, especially for attack samples. This paper introduces a teacher-student framework to improve the cross-domain performance of face PAD with one-class domain adaptation. In addition to the source domain data, the framework utilizes only a few genuine face samples of the target domain. Under this framework, a teacher network is trained with source domain samples to provide discriminative feature representations for face PAD. Student networks are trained to mimic the teacher network and learn similar representations for genuine face samples of the target domain. In the test phase, the similarity score between the representations of the teacher and student networks is used to distinguish attacks from genuine ones. To evaluate the proposed framework under one-class domain adaptation settings, we devised two new protocols and conducted extensive experiments. The experimental results show that our method outperforms baselines under one-class domain adaptation settings and even state-of-the-art methods with unsupervised domain adaptation.

## What does the paper present?
## What are my views on it?
