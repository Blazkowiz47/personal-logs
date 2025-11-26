---
tags: [survey, pad, deep-fas]
status: 📚 To Read
---

# 👏 Survey of Deep Face Anti-spoofing 🔥

This is the official repository of "**[Deep Learning for Face Anti-Spoofing: A Survey](https://arxiv.org/abs/2106.14948)**", a comprehensive survey 
of recent progress in deep learning methods for face anti-spoofing (FAS) as well as the datasets and protocols.



### Citation
If you find our work useful in your research, please consider citing:

    @article{yu2022deep,
      title={Deep Learning for Face Anti-Spoofing: A Survey},
      author={Yu, Zitong and Qin, Yunxiao and Li, Xiaobai and Zhao, Chenxu and Lei, Zhen and Zhao, Guoying},
      journal={IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)},
      year={2022}
    }


## Introduction
We present a comprehensive review of recent deep learning methods for face anti-spoofing (mostly from 2018 to 2022). It covers hybrid (handcrafted+deep), pure deep learning, and generalized learning based methods for monocular RGB face anti-spoofing. It also includes multi-modal learning based methods as well as specialized sensor based FAS. It also presents detailed comparision among publicly available datasets, together with several classical evaluation protocols.

🔔 We will update this page frequently~ :tada::tada::tada:

---
## Contents

- [Datasets](#data)
  - [Using commercial RGB camera](#data_RGB)
  - [With multiple modalities or specialized sensors](#data_Multimodal)
- [Deep FAS methods with commercial RGB camera](#methods_RGB)
  - [Hybrid (handcrafted + deep)](#hybrid)
  - [End-to-end binary cross-entropy supervision](#binary)
  - [Pixel-wise auxiliary supervision](#auxiliary)
  - [Generative model with pixel-wise supervision](#generative)
  - [Domain adaptation](#DA)
  - [Domain generalization](#DG)
  - [Zero/Few-shot learning](#zero-shot)
  - [Anomaly detection](#oneclass)
  - [Semi-supervision & Self-supervision](#semiself)
  - [Continual learning](#CL)
- [Deep FAS methods with advanced sensor](#methods_advanced)
  - [Learning upon specialized sensor](#sensor)
  - [Multi-modal learning](#multimodal)
  - [Flexible-modal learning](#flexmodal)

---
![[DeepFAS-Topology.png]]
  
---


<a name="data" />

### 1️⃣ Datasets

<a name="data_RGB" />

#### Datasets recorded with commercial RGB camera

| Dataset    | Year | #Live/Spoof | #Sub. |  Setup | Attack Types |
| --------   | -----    | -----  |  -----  | ----- |------------------------|
| [NUAA](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.607.5449&rep=rep1&type=pdf) | 2010 | 5105/7509(I) | 15 | N/R | Print(flat, wrapped) |
| [YALE Recaptured](https://www.ic.unicamp.br/~rocha/pub/papers/2011-icip-spoofing-detection.pdf) | 2011 | 640/1920(I) | 10 | 50cm-distance from 3 LCD minitors | Print(flat) |
| [[Casia-fasd|CASIA-MFSD]] | 2012 | 150/450(V) | 50 | 7 scenarios and 3 image quality | Print(flat, wrapped, cut), Replay(tablet) |
| [[Idiap Replay-Attack|REPLAY-ATTACK]] | 2012 | 200/1000(V) | 50 | Lighting and holding | Print(flat), Replay(tablet, phone) |
| [Kose and Dugelay](https://ieeexplore.ieee.org/document/6595862) | 2013 | 200/198(I) | 20 | N/R | Mask(hard resin) |
| [[MSU-MFSD|MSU-MFSD]] | 2014 | 70/210(V) | 35 | Indoor scenario; 2 types of cameras | Print(flat), Replay(tablet, phone) |
| [UVAD](https://ieeexplore.ieee.org/document/7017526) | 2015 | 808/16268(V) | 404 | Different lighting, background and places in two sections | Replay(monitor) |
| [REPLAY-Mobile](https://ieeexplore.ieee.org/document/7736936) | 2016 | 390/640(V) | 40 | 5 lighting conditions | Print(flat), Replay(monitor) |
| [HKBU-MARs V2](https://link.springer.com/chapter/10.1007/978-3-319-46478-7_6) | 2016 | 504/504(V) | 12 | 7 cameras from stationary and mobile devices and 6 lighting settings | Mask(hard resin) from Thatsmyface and REAL-f |
| [MSU USSA](https://ieeexplore.ieee.org/document/7487030) | 2016 | 1140/9120(I) | 1140 | Uncontrolled; 2 types of cameras | Print(flat), Replay(laptop, tablet, phone) |
| [SMAD](https://ieeexplore.ieee.org/document/7867821) | 2017 | 65/65(V) | - | Color images from online resources | Mask(silicone) |
| [[Oulu-NPU|OULU-NPU]] | 2017 | 720/2880(V) | 55 | Lighting & background in 3 sections | Print(flat), Replay(phone) |
| [Rose-Youtu](https://ieeexplore.ieee.org/document/8279564) | 2018 | 500/2850(V) | 20 | 5 front-facing phone camera; 5 different illumination conditions | Print(flat), Replay(monitor, laptop),Mask(paper, crop-paper) |
| [[SiW|SiW]] | 2018 | 1320/3300(V) | 165 | 4 sessions with variations of distance, pose, illumination and expression | Print(flat, wrapped), Replay(phone, tablet, monitor) |
| [WFFD](https://arxiv.org/abs/2005.06514) | 2019 | 2300/2300(I) 140/145(V) | 745 | Collected online; super-realistic; removed low-quality faces | Waxworks(wax) |
| [[SiW-M|SiW-M]] | 2019 | 660/968(V) | 493 | Indoor environment with pose, lighting and expression variations | Print(flat), Replay, Mask(hard resin, plastic, silicone, paper, Mannequin), Makeup(cosmetics, impersonation, Obfuscation), Partial(glasses, cut paper) |
| [Swax](https://arxiv.org/abs/1910.09642) | 2020 | Total 1812(I) 110(V) | 55 | Collected online; captured under uncontrolled scenarios | Waxworks(wax) |
| [[CelebA-Spoof|CelebA-Spoof]] | 2020 | 156384/469153(I) | 10177 | 4 illumination conditions; indoor & outdoor; rich annotations | Print(flat, wrapped), Replay(monitor tablet, phone), Mask(paper) |
| [RECOD-Mtablet](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0238058) | 2020 | 450/1800(V) | 45 | Outdoor environment and low-light & dynamic sessions | Print(flat), Replay(monitor) |
| [CASIA-SURF 3DMask](https://ieeexplore.ieee.org/document/9252183) | 2020 | 288/864(V) | 48 | High-quality identity-preserved; 3 decorations and 6 environments | Mask(mannequin with 3D print) |
| [HiFiMask](https://arxiv.org/abs/2104.06148) | 2021 | 13650/40950(V) | 75 | three mask decorations; 7 recording devices; 6 lighting conditions; 6 scenes | Mask(transparent, plaster, resin) |
| [SiW-M v2](https://github.com/CHELSEA234/Multi-domain-learning-FAS) | 2022 | 785/915 (V) | 1093(493/600) | Both indoor and outdoor, diverse age and enthnicity, 7 illumiations | IAPRA-verified 14 spoof attacks (4 coverings, 3 makeups, 3 masks, 2 human models, replay and print) |
| [SuHiFiMask](https://arxiv.org/abs/2301.00975) | 2022 | 10195/10195 (V) | 101 | Long distance using Surveillance cameras, recording in 3 scenes, and 3 lightings, 4 whethers | 2D image, Video replay, 3D Mask with materials Resin, Plaster, Silicone, Paper |
| [WFAS](https://arxiv.org/abs/2304.05753) | 2023 | 529,571/ 853,729 (I) | 469,920 | Internet, unconstrained settings | 17 PAs, Print(newspaper, poster, photo, album, picture book, scan photo, packging, cloth), Display(phone, tablet, TV, computer), Mask, 3D Model(garage kit, doll, adult doll, waxwork) |


<a name="data_Multimodal" />

#### Datasets with multiple modalities or specialized sensors

| Dataset    | Year | #Live/Spoof | #Sub. |  M&H | Setup | Attack Types |
| --------   | -----    | -----  |  -----  | -----  | -----  |------------------------|
| [3DMAD](https://ieeexplore.ieee.org/document/6810829) | 2013 | 170/85(V) | 17 | VIS, Depth | 3 sessions (2 weeks interval) | Mask(paper, hard resin) |
| [GUC-LiFFAD](https://ieeexplore.ieee.org/document/7018027) | 2015 | 1798/3028(V) | 80 | Light field | Distance of 1.5 constrained conditions | Print(Inkjet paper, Laserjet paper), Replay(tablet) |
| [3DFS-DB](https://www.researchgate.net/publication/277905873_Three-dimensional_and_two-and-a-half-dimensional_face_recognition_spoofing_using_three-dimensional_printed_models) | 2016 | 260/260(V) | 26 | VIS, Depth | Head movement with rich angles | Mask(plastic) |
| [BRSU Skin/Face/Spoof](https://ieeexplore.ieee.org/document/7550052) | 2016 | 102/404(I) | 137 | VIS, SWIR | multispectral SWIR with 4 wavebands 935nm, 1060nm, 1300nm and 1550nm | Mask(silicon, plastic, resin, latex) |
| [Msspoof](https://link.springer.com/chapter/10.1007/978-3-319-28501-6_8) | 2016 | 1470/3024(I) | 21 | VIS, NIR | 7 environmental conditions | Black&white Print(flat) |
| [MLFP](https://ieeexplore.ieee.org/document/8014774) | 2017 | 150/1200(V) | 10 | VIS, NIR, Thermal | Indoor and outdoor with fixed and random backgrounds | Mask(latex, paper) |
| [ERPA](https://www.researchgate.net/publication/320177829_What_You_Can't_See_Can_Help_You_-_Extended-Range_Imaging_for_3D-Mask_Presentation_Attack_Detection) | 2017 | Total 86(V) | 5 | VIS, Depth, NIR, Thermal | Subject positioned close (0.3∼0.5m) to the 2 types of cameras | Print(flat), Replay(monitor), Mask(resin, silicone) |
| [LF-SAD ](http://www.ee.cityu.edu.hk/~lmpo/publications/2019_JEI_Face_Liveness.pdf) | 2018 | 328/596(I) | 50 | Light field | Indoor fix background, captured by Lytro ILLUM camera | Print(flat, wrapped), Replay(monitor) |
| [CSMAD](https://ieeexplore.ieee.org/document/8698550) | 2018 | 104/159(V+I) | 14 | VIS, Depth, NIR, Thermal | 4 lighting conditions | Mask(custom silicone) |
| [3DMA](https://ieeexplore.ieee.org/document/8909845) | 2019 | 536/384(V) | 67 | VIS, NIR | 48 masks with different ID; 2 illumination & 4 capturing distances | Mask(plastics) |
| [[CASIA-SURF|CASIA-SURF]] | 2019 | 3000/18000(V) | 1000 | VIS, Depth, NIR | Background removed; Randomly cut eyes, nose or mouth areas | Print(flat, wrapped, cut) |
| [[WMCA|WMCA]] | 2019 | 347/1332(V) | 72 | VIS, Depth, NIR, Thermal | 6 sessions with different backgrounds and illumination; pulse data for bonafide recordings | Print(flat), Replay(tablet), Partial(glasses), Mask(plastic, silicone, and paper, Mannequin) |
| [[CASIA-SURF CeFA|CeFA]] | 2020 | 6300/27900(V) | 1607 | VIS, Depth, NIR | 3 ethnicities; outdoor & indoor; decoration with wig and glasses | Print(flat, wrapped), Replay, Mask(3D print, silica gel) |
| [HQ-WMCA](https://ieeexplore.ieee.org/abstract/document/9146362) | 2020 | 555/2349(V) | 51 | VIS, Depth, NIR, SWIR, Thermal | Indoor; 14 ‘modalities’, including 4 NIR and 7 SWIR wavelengths; masks and mannequins were heated up to reach body temperature | Laser or inkjet Print(flat), Replay(tablet, phone), Mask(plastic, silicon, paper, mannequin), Makeup, Partial(glasses, wigs, tatoo) |
| [PADISI-Face](https://arxiv.org/pdf/2108.12081.pdf) | 2021 | 1105/924(V) | 360 | VIS, Depth, NIR, SWIR, Thermal | Indoor, fixed background, 60-frame sequence of 1984 × 1264 pixel images | print(flat), replay(tablet, phone), mask(plastic, silicon, transparent, Mannequin), makeup/tatoo, partial(glasses,funny eye) |



---
<a name="methods_RGB" />

### 2️⃣ Deep FAS methods with commercial RGB camera

- temp

<a name="hybrid" />

#### Hybrid (handcrafted + deep)

| Method    | Year | Backbone | Loss |  Input | Static/Dynamic |
| --------   | -----    | -----  |  -----  | -----  | -----  |
| [[DPCNN (2016)|DPCNN]] | 2016 | VGG-Face | Trained with SVM | RGB | S |
| [[Multi-cues+NN (2016)|Multi-cues+NN]] | 2016 | MLP | Binary CE loss | RGB+OFM | D |
| [[CNN LBP-TOP (2017)|CNN LBP-TOP]] | 2017 | 5-layer CNN | Binary CE loss, SVM | RGB | D |
| [[DF-MSLBP (2018)|DF-MSLBP]] | 2018 | Deep forest | Binary CE loss | HSV+YCbCr | S |
| [[SPMT+SSD (2018)|SPMT+SSD]] | 2018 | VGG16 | Binary CE loss, SVM, bbox regression | RGB, Landmarks | S |
| [[CHIF (2019)|CHIF]] | 2019 | VGG-Face | Trained with SVM | RGB | S |
| [[DeepLBP (2019)|DeepLBP]] | 2019 | VGG-Face | Binary CE loss, SVM | RGB, HSV, YCbCr | S |
| [[CNN+LBP+WLD (2019)|CNN+LBP+WLD]] | 2019 | CaffeNet | Binary CE loss | RGB | S |
| [[Intrinsic (2019)|Intrinsic]] | 2019 | 1D-CNN | Trained with SVM | Reflection | D |
| [[FARCNN (2019)|FARCNN]] | 2019 | Multi-scale attentional CNN | Regression loss, Crystal loss, Center loss | RGB | S |
| [[CNN-LSP (TIFS 2019)|CNN-LSP]] | TIFS 2019 | 1D-CNN | Trained with SVM | RGB | D |
| [[DT-Mask (2019)|DT-Mask]] | 2019 | VGG16 | Binary CE loss, Channel&Spatial discriminability | RGB+OF | D |
| [[VGG+LBP (2019)|VGG+LBP]] | 2019 | VGG16 | Binary CE loss | RGB | S |
| [[CNN+OVLBP (2019)|CNN+OVLBP]] | 2019 | VGG16 | Binary CE loss, NN classifier | RGB | S |
| [[HOG-Pert. (2019)|HOG-Pert.]] | 2019 | Multi-scale CNN | Binary CE loss | RGB+HOG | S |
| [[LBP-Pert. (2020)|LBP-Pert.]] | 2020 | Multi-scale CNN | Binary CE loss | RGB+LBP | S |
| [[TransRPPG (SPL 2021)|TransRPPG]] | SPL 2021 | Vision Transformer | Binary CE loss | rPPG map | D |



<a name="binary" />

#### End-to-end binary cross-entropy supervision
| Method    | Year | Backbone | Loss |  Input | Static/Dynamic |
| --------   | -----    | -----  |  -----  | -----  | -----  |
| [[CNN1 (2014)|CNN1]] | 2014 | 8-layer CNN | Trained with SVM | RGB | S |
| [[LSTM-CNN (2015)|LSTM-CNN]] | 2015 | CNN+LSTM | Binary CE loss | RGB | D |
| [[SpoofNet (2015)|SpoofNet]] | 2015 | 2-layer CNN | Binary CE loss | RGB | S |
| [[HybridCNN (2017)|HybridCNN]] | 2017 | VGG-Face | Trained with SVM | RGB | S |
| [[CNN2 (2017)|CNN2]] | 2017 | VGG11 | Binary CE loss | RGB | S |
| [[Ultra-Deep (2017)|Ultra-Deep]] | 2017 | ResNet50+LSTM | Binary CE loss | RGB | D |
| [[FASNet (2017)|FASNet]] | 2017 | VGG16 | Binary CE loss | RGB | S |
| [[CNN3 (2018)|CNN3]] | 2018 | Inception, ResNet | Binary CE loss | RGB | S |
| [[MILHP (2018)|MILHP]] | 2018 | ResNet+STN | Multiple Instances CE loss | RGB | D |
| [[LSCNN (2018)|LSCNN]] | 2018 | 9 PatchNets | Binary CE loss | RGB | S |
| [[LiveNet (2018)|LiveNet]] | 2018 | VGG11 | Binary CE loss | RGB | S |
| [[MS-FANS  (2018)|MS-FANS ]] | 2018 | AlexNet+LSTM | Binary CE loss | RGB | S |
| [[DeepColorFAS (2018)|DeepColorFAS]] | 2018 | 5-layer CNN | Binary CE loss | RGB, HSV, YCbCr | S |
| [[Siamese (2019)|Siamese]] | 2019 | AlexNet | Contrastive loss | RGB | S |
| [[FSBuster (2019)|FSBuster]] | 2019 | ResNet50 | Trained with SVM | RGB | S |
| [[FuseDNG (2019)|FuseDNG]] | 2019 | 7-layer CNN | Binary CE loss, Reconstruction loss | RGB | S |
| [[STASN (CVPR 2019)|STASN]] | CVPR 2019 | ResNet50+LSTM | Binary CE loss | RGB | D |
| [[TSCNN (TIFS 2019)|TSCNN]] | TIFS 2019 | ResNet18 | Binary CE loss | RGB, MSR | S |
| [[FAS-UCM (2019)|FAS-UCM]] | 2019 | MobileNetV2, VGG19 | Binary CE loss, Style loss | RGB | S |
| [[SLRNN (2019)|SLRNN]] | 2019 | ResNet50+LSTM | Binary CE loss | RGB | D |
| [[GFA-CNN (2019)|GFA-CNN]] | 2019 | VGG16 | Binary CE loss | RGB | S |
| [[3DSynthesis (2019)|3DSynthesis]] | 2019 | ResNet15 | Binary CE loss | RGB | S |
| [[CompactNet (NC 2020)|CompactNet]] | NC 2020 | VGG19 | Points-to-Center triplet loss | RGB | S |
| [[SSR-FCN (TIFS 2020)|SSR-FCN]] | TIFS 2020 | FCN with 6 layers | Binary CE loss | RGB | S |
| [[FasTCo (2020)|FasTCo]] | 2020 | ResNet50 or MobileNetV2 | Multi-class CE loss, Temporal Consistency loss, Class Consistency loss | RGB | D |
| [[DRL-FAS (TIFS 2020)|DRL-FAS]] | TIFS 2020 | ResNet18+GRU | Binary CE loss | RGB | S |
| [[SfSNet (2020)|SfSNet]] | 2020 | 6-layer CNN | Binary CE loss | Albedo, Depth, Reflection | S |
| [[LivenesSlight (2020)|LivenesSlight]] | 2020 | 6-layer CNN | Binary CE loss | RGB | S |
| [[MotionEnhancement (2020)|MotionEnhancement]] | 2020 | VGGface+LSTM | Binary CE loss | RGB | D |
| [[CFSA-FAS (2020)|CFSA-FAS]] | 2020 | ResNet18 | Binary CE loss | RGB | S |
| [[MC-FBC (2020)|MC-FBC]] | 2020 | VGG16, ResNet50 | Binary CE loss | RGB | S |
| [[SimpleNet (2020)|SimpleNet]] | 2020 | Multi-stream 5-layer CNN | Binary CE loss | RGB, OF, RP | D |
| [[PatchCNN (2020)|PatchCNN]] | 2020 | SqueezeNet v1.1 | Binary CE loss, Triplet loss | RGB | S |
| [[FreqSpatialTempNet (2020)|FreqSpatialTempNet]] | 2020 | ResNet18 | Binary CE loss | RGB, HSV, Spectral | D |
| [[ViTranZFAS (IJCB 2021)|ViTranZFAS]] | IJCB 2021 | ViT | Binary CE loss | RGB | S |
| [[CIFL (TIFS 2021)|CIFL]] | TIFS 2021 | ResNet18 | Binary focal loss, camear type loss | RGB | S |
| [[XFace-PAD (FG 2021)|XFace-PAD]] | FG 2021 | ResNet50, ViT | Binary CE loss, word-wise CE loss, a sentence discriminative loss, and a sentence semantic loss | RGB | S |
| [[PCGN (MM 2021)|PCGN]] | MM 2021 | ResNet101+GCN | CE Loss for node and edge | RGB whole image | S |
| [[TOD (2021)|TOD]] | 2021 | ResNet18, Graph Attention Network | CE Loss | RGB | S |
| [[MTSS (BMVC 2021)|MTSS]] | BMVC 2021 | ViT+Multi-Level Attention Module | CE Loss | RGB | S |
| [[PatchNet (CVPR 2022)|PatchNet]] | CVPR 2022 | ResNet18 | Asymmetric AM-Softmax Loss, Self-Supervised Similarity Loss | RGB patches | S |
| [[ViTransPAD (ICIP 2022)|ViTransPAD]] | ICIP 2022 | EfficientNet + VideoViT | CE Loss | RGB | D |
| [[FGDNet (TMM 2022)|FGDNet]] | TMM 2022 | Convolutional Transformer | 5-class CE Loss | RGB | S |

<a name="auxiliary" />

#### Pixel-wise auxiliary supervision

| Method    | Year | Supervision | Backbone |  Input | Static/Dynamic |
| --------   | -----    | -----  |  -----  | -----  | -----  |
| [[Depth&Patch (IJCB 2017)|Depth&Patch]] | IJCB 2017 | Depth | PatchNet, DepthNet | YCbCr, HSV | S |
| [[Auxiliary (CVPR 2018)|Auxiliary]] | CVPR 2018 | Depth, rPPG spectrum | DepthNet | RGB, HSV | D |
| [[BASN (ICCVW 2019)|BASN]] | ICCVW 2019 | Depth, Reflection | DepthNet, Enrichment | RGB, HSV | S |
| [[DTN (CVPR 2019)|DTN]] | CVPR 2019 | BinaryMask | Tree Network | RGB, HSV | S |
| [[PixBiS (ICB 2019)|PixBiS]] | ICB 2019 | BinaryMask | DenseNet161 | RGB | S |
| [[A-PixBiS (2020)|A-PixBiS]] | 2020 | BinaryMask | DenseNet161 | RGB | S |
| [[Auto-FAS (ICASSP 2020)|Auto-FAS]] | ICASSP 2020 | BinaryMask | NAS | RGB | S |
| [[MRCNN (2020)|MRCNN]] | 2020 | BinaryMask | Shallow CNN | RGB | S |
| [[FCN-LSA (2020)|FCN-LSA]] | 2020 | BinaryMask | DepthNet | RGB | S |
| [[CDCN (CVPR 2020)|CDCN]] | CVPR 2020 | Depth | DepthNet | RGB | S |
| [[FAS-SGTD (CVPR 2020)|FAS-SGTD]] | CVPR 2020 | Depth | DepthNet, STPM | RGB | D |
| [[TS-FEN (2020)|TS-FEN]] | 2020 | Depth | ResNet34, FCN | RGB, YCbCr, HSV | S |
| [[SAPLC (2020)|SAPLC]] | 2020 | TernaryMap | DepthNet | RGB, HSV | S |
| [[BCN (ECCV 2020)|BCN]] | ECCV 2020 | BinaryMask, Depth, Reflection | DepthNet | RGB | S |
| [[Disentangled (ECCV 2020)|Disentangled]] | ECCV 2020 | Depth, TextureMap | DepthNet | RGB | S |
| [[AENet (ECCV 2020)|AENet]] | ECCV 2020 | Depth, Reflection | ResNet18 | RGB | S |
| [[3DPC-Net (IJCB 2020)|3DPC-Net]] | IJCB 2020 | 3D Point Cloud | ResNet18 | RGB | S |
| [[PS (TBIOM 2020)|PS]] | TBIOM 2020 | BinaryMask or Depth | ResNet50 or CDCN | RGB | S |
| [[NAS-FAS (PAMI 2020)|NAS-FAS]] | PAMI 2020 | BinaryMask or Depth | NAS | RGB | D |
| [[DAM (2021)|DAM]] | 2021 | Depth | VGG16, TSM | RGB | D |
| [[Bi-FPNFAS (2021)|Bi-FPNFAS]] | 2021 | Fourier spectra | EfficientNetB0, FPN | RGB | S |
| [[DC-CDN (IJCAI 2021)|DC-CDN]] | IJCAI 2021 | Depth | CDCN | RGB | S |
| [[DCN (IJCB 2021)|DCN]] | IJCB 2021 | Reflection | DepthNet | RGB | S |
| [[LMFD-PAD (2021)|LMFD-PAD]] | 2021 | BinaryMask | Dual-ResNet50 | RGB + frequency map | S |
| [[MPFLN (ICCVW 2021)|MPFLN]] | ICCVW 2021 | Depth, BinaryMask | CDCN, 3D-CDCN | RGB | S, D |
| [[DSDG+DUM (TIFS 2021)|DSDG+DUM]] | TIFS 2021 | Depth | CDCN | RGB | S |
| [[SAFPAD (TIFS 2021)|SAFPAD]] | TIFS 2021 | Depth | DepthNet | RGB & Patch | S |
| [[EPCR (2021)|EPCR]] | 2021 | BinaryMask | CDCN | RGB | S |
| [[AISL (PRL 2021)|AISL]] | PRL 2021 | Depth | DepthNet | RGB | S |
| [[MEGC (ICASSP 2022)|MEGC]] | ICASSP 2022 | Depth, Relection, Moire, Boundary | DepthNet+Feature Enrichment | RGB, HSV | S |
| [[EulerNet (2022)|EulerNet]] | 2022 | Face Location Map | EulerNet with Temporal Attention, Residual Pyramid | RGB | D |
| [[TTN (TIFS 2022)|TTN]] | TIFS 2022 | Depth | ViT with Pyramid Temporal Aggregation, Temporal Difference Attentions | RGB | D |
| [[TransFAS (TBIOM 2022)|TransFAS]] | TBIOM 2022 | Depth | ViT with Cross-Layer Attentions | RGB | S |
| [[DepthSeg (IJCNN 2022)|DepthSeg]] | IJCNN 2022 | Depth | PSPNet, DeepLabv3+ | RGB | S |


<a name="generative" />

#### Generative model with pixel-wise supervision

| Method    | Year | Supervision | Backbone |  Input | Static/Dynamic |
| --------   | -----    | -----  |  -----  | -----  | -----  |
| [[De-Spoof (ECCV 2018)|De-Spoof]] | ECCV 2018 | Depth, BinaryMask, FourierMap | DSNet, DepthNet | RGB, HSV | S |
| [[Reconstruction (2019)|Reconstruction]] | 2019 | RGB Input (live), ZeroMap (spoof) | U-Net | RGB | S |
| [[LGSC (2020)|LGSC]] | 2020 | ZeroMap (live) | U-Net, ResNet18 | RGB | S |
| [[TAE (ICASSP 2020)|TAE]] | ICASSP 2020 | Binary CE loss, Reconstruction loss | Info-VAE, DenseNet161 | RGB | S |
| [[STDN (ECCV 2020)|STDN]] | ECCV 2020 | BinaryMask, RGB Input (live) | U-Net, PatchGAN | RGB | S |
| [[GOGen (CVPR 2020)|GOGen]] | CVPR 2020 | RGB input | DepthNet | RGB+one-hot vector | S |
| [[PhySTD (PAMI 2022)|PhySTD]] | PAMI 2022 | Depth, RGB Input (live) | U-Net, PatchGAN | Frequency Trace | S |
| [[MT-FAS (PAMI 2021)|MT-FAS]] | PAMI 2021 | ZeroMap (live), LearnableMap (Spoof) | DepthNet | RGB | S |
| [[IF-OM (2021)|IF-OM]] | 2021 | RGB input, mixed input features | MobileNetV2 + UNet | RGB, mixed RGB, folded RGB | S |
| [[Dual-Stage Disentanglement (WACV 2021)|Dual-Stage Disentanglement]] | WACV 2021 | ZeroMap (live), RGB Input for reconstruction | U-Net, ResNet18 | RGB | S |


<a name="DA" />

#### Domain adaptation

| Method    | Year | Backbone | Loss |  Static/Dynamic |
| --------   | -----    | -----  |  -----  | -----  | 
| [[OR-DA (TIFS 2018)|OR-DA]] | TIFS 2018 | AlexNet | Binary CE loss, MMD loss | S |
| [[DTCNN (2019)|DTCNN]] | 2019 | AlexNet | Binary CE loss, MMD loss | S |
| [[Adversarial (ICB 2019)|Adversarial]] | ICB 2019 | ResNet18 | Triplet loss, Adversarial loss | S |
| [[ML-MMD (ICMEW 2019)|ML-MMD]] | ICMEW 2019 | Multi-scale FCN | CE loss, MMD loss | S | and unlabeled sets |
| [[OCA-FAS (NC 2020)|OCA-FAS]] | NC 2020 | DepthNet | Binary CE loss, Pixel-wise binary loss | S |
| [[DR-UDA (TIFS 2020)|DR-UDA]] | TIFS 2020 | ResNet18 | Center&Triplet loss, Adversarial loss, Disentangled loss | S |
| [[DGP (ICASSP 2020)|DGP]] | ICASSP 2020 | DenseNet161 | Feature divergence measure, BinaryMask loss | S |
| [[Distillation (J-STSP 2020)|Distillation]] | J-STSP 2020 | AlexNet | Binary CE loss, MMD loss , Paired Similarity | S |
| [[SASA (2021)|SASA]] | 2021 | ResNet18 | CE Loss, Adversarial loss, Less-forgetting constraints, Contrastive semantic alignment | S |
| [[GDA (ECCV 2022)|GDA]] | ECCV 2022 | DepthNet | CE Loss, Depth loss, Inter-domain Neural Statistic Consistency, phase consistency, Perceptual loss | S |
| [[CDFTN (AAAI 2023)|CDFTN]] | AAAI 2023 | ResNet18 | CE Loss, Reconstruction loss, triplet loss | S |



<a name="DG" />

#### Domain generalization


| Method    | Year | Backbone | Loss |  Static/Dynamic |
| --------   | -----    | -----  |  -----  | -----  | 
| [[MADDG (CVPR 2019)|MADDG]] | CVPR 2019 | DepthNet | Binary CE & Depth loss, Multi-adversarial loss, Dual-force Triplet loss | S |
| [[PAD-GAN (CVPR 2020)|PAD-GAN]] | CVPR 2020 | ResNet18 | Binary CE & Depth loss, Multi-adversarial loss, Dual-force Triplet loss | S |
| [[DASN (2020)|DASN]] | 2020 | ResNet18 | Binary CE & Spoof-irrelevant factor loss | S |
| [[SSDG (CVPR 2020)|SSDG]] | CVPR 2020 | ResNet18 | Binary CE loss, Single-Side adversarial loss, Asymmetric Triplet loss | S |
| [[RF-Meta (AAAI 2020)|RF-Meta]] | AAAI 2020 | DepthNet | Binary CE loss, Depth loss | S |
| [[CCDD (CVPRW 2020)|CCDD]] | CVPRW 2020 | ResNet50+LSTM | Binary CE loss, Class-conditional loss | D |
| [[SDA (AAAI 2021)|SDA]] | AAAI 2021 | DepthNet | Binary CE & Depth loss, Reconstruction loss, Orthogonality regularization | S |
| [[D2AM (AAAI 2021)|D2AM]] | AAAI 2021 | DepthNet | Binary CE loss, Depth loss, MMD loss | S |
| [[DRDG (IJCAI 2021)|DRDG]] | IJCAI 2021 | DepthNet | Binary CE loss, Depth loss, Domain loss | S |
| [[PDL-FAS (2021)|PDL-FAS]] | 2021 | DepthNet | Binary CE loss, Depth loss | S |
| [[ANRL (ACMMM 2021)|ANRL]] | ACMMM 2021 | DepthNet | Binary CE loss, Depth loss, Inter-Domain Compatible Loss, Inter-Class Separable Loss | S |
| [[HFN+MP (2021)|HFN+MP]] | 2021 | Two-stream ResNet50 | Binary CE loss, MSE loss | S |
| [[SDFANet (TIFS 2021)|SDFANet]] | TIFS 2021 | ResNet-18 | BCE loss + multi-grained loss + center loss + asymmetric triplet loss | S |
| [[VLAD-VSA (ACMMM 2021)|VLAD-VSA]] | ACMMM 2021 | DepthNet or ResNet18 | BCE loss + triplet loss + domain adversarial loss + orthogonal loss +  centroid adaptation loss + intra loss | S |
| [[FGHV (AAAI 2022)|FGHV]] | AAAI 2022 | DepthNet | Variance + Relative Correlation + Distribution Discrimination Constraints | S |
| [[SSAN (CVPR 2022)|SSAN]] | CVPR 2022 | DepthNet/ResNet18 | CE loss + Domain Adversarial loss + Contrastive loss | S |
| [[AMEL (ACMMM 2022)|AMEL]] | ACMMM 2022 | DepthNet | CE loss, Depth loss, Feature consistency loss | S |
| [[MD-FAS (ECCV 2022)|MD-FAS]] | ECCV 2022 | PhySTD | CE loss, Binary Mask loss, Source & Target distillation loss | S |
| [[FRT-PAD (ECCV 2022)|FRT-PAD]] | ECCV 2022 | ResNet18+GAT | CE loss | S |
| [[CIFAS (ICME 2022)|CIFAS]] | ICME 2022 | ResNet18 | CE loss, triplet loss | S |
| [[OneSideTriplet (FG 2023)|OneSideTriplet]] | FG 2023 | DepthNet+UNet | CE loss, triplet loss, Depth loss, Segmentation loss | S |
| [[DiVT (WACV 2023)|DiVT]] | WACV 2023 | MobileViT-S | Domain-invariant Concentration and Attack-separation Loss | S |
| [[ALDICF (IJCV 2023)|ALDICF]] | IJCV 2023 | ResNet18, ResNet50 | Intra-domain and cross-domain discrimination loss, Conditional Domain Adversarial loss | S |
| [[DKG+CSA+AIAW (CVPR 2023)|DKG+CSA+AIAW]] | CVPR 2023 | DepthNet | BCE loss, Depth loss, Asymmetric Instance Adaptive Whiting loss | S |
| [[SA-FAS (CVPR 2023)|SA-FAS]] | CVPR 2023 | ResNet18 | Contrastive loss, Alignment loss | S |
| [[SPDA (ICASSP 2023)|SPDA]] | ICASSP 2023 | ResNet18 | BCE loss, Domain loss, Self-paced Cluster Mining loss, orthogonal loss | S |
| [[CRFAS (ICASSP 2023)|CRFAS]] | ICASSP 2023 | ResNet18 | BCE loss, Domain loss,  asymmetric triplet loss, Counterfactual Feature Generation loss | S |

<a name="zero-shot" />

#### Zero/Few-shot learning


| Method    | Year | Backbone | Loss |  Input |
| --------   | -----    | -----  |  -----  | -----  | 
| [[DTN (CVPR 2019)|DTN]] | CVPR 2019 | Deep Tree Network | Binary CE loss, Pixel-wise binary loss, Unsupervised Tree loss | RGB, HSV |
| [[AIM-FAS (AAAI 2020)|AIM-FAS]] | AAAI 2020 | DepthNet | Depth loss, Contrastive Depth loss | RGB |
| [[CM-PAD (IJCB 2021)|CM-PAD]] | IJCB 2021 | DepthNet, ResNet | Binary CE loss, Depth loss, Gradient alignment | RGB |
| [[ViTAF (ECCV 2022)|ViTAF]] | ECCV 2022 | ViT+adaptor | CE Loss,  Cosine loss | S |




<a name="oneclass" />

#### Anomaly detection


| Method    | Year | Backbone | Loss |  Input |
| --------   | -----    | -----  |  -----  | -----  | 
| [[AE+LBP (2018)|AE+LBP]] | 2018 | AutoEncoder | Reconstruction loss | RGB |
| [[Anomaly (2019)|Anomaly]] | 2019 | ResNet50 | Triplet focal loss, Metric-Softmax loss | RGB |
| [[Anomaly2 (2019)|Anomaly2]] | 2019 | GoogLeNet or ResNet50 | Mahalanobis distance | RGB |
| [[Hypersphere (2020)|Hypersphere]] | 2020 | ResNet18 | Hypersphere loss | RGB, HSV |
| [[Ensemble-Anomaly (2020)|Ensemble-Anomaly]] | 2020 | GoogLeNet or ResNet50 | Gaussian Mixture Model (not end-to-end) | RGB, patches |
| [[MCCNN (2020)|MCCNN]] | 2020 | LightCNN | Binary CE loss, Contrastive loss | Grayscale, IR, Depth, Thermal |
| [[End2End-Anomaly (2020)|End2End-Anomaly]] | 2020 | VGG-Face | Binary CE loss, Pairwise confusion | RGB |
| [[ClientAnomaly (PR 2020)|ClientAnomaly]] | PR 2020 | ResNet50 or GoogLeNet or VGG16 | One-class SVM or Mahalanobis distance or Gaussian Mixture Model | RGB |
| [[ContrastiveEVT (ACM MM 2021)|ContrastiveEVT]] | ACM MM 2021 | cVAE | Binary CE loss, reconstruction loss, contrastive loss | RGB |
| [[OneClassKD (TIFS 2022)|OneClassKD]] | TIFS 2022 | DepthNet | Pixel-wise Binary CE loss, multi-level KD loss | RGB |


<a name="semiself" />

#### Semi- & Self-supervision


| Method    | Year | Semi/Self | Backbone | Loss |  
| --------   | -----    | -----  |  -----  | -----  | 
| [[SCNN++PL+TC (TIP 2021)|SCNN++PL+TC]] | TIP 2021 | Semi; Pseudo-label | ResNet18 | CE Loss |
| [[USDAN (PR 2021)|USDAN]] | PR 2021 | Semi; Distribution Alignment | ResNet18 | Adaptive binary CE loss, Entropy loss, Adversarial loss |
| [[EPCR (TIFS 2023)|EPCR]] | TIFS 2023 | Semi; Consistency Regularization | CDCN | Prediction- & Embedding-level reconstruction loss |
| [[TSS (PRL 2022)|TSS]] | PRL 2022 | Self; Pretext task | ResNet18+BiLSTM | CE loss for temporal sampling prediction |
| [[ACL-FAS (PRCV 2022)|ACL-FAS]] | PRCV 2022 | Self; Contrastive learning | - | Region-Based Similarity Loss, Contrastive & Anti-contrastive loss |
| [[MIM-FAS (PRCV 2022)|MIM-FAS]] | PRCV 2022 | Self; Masked Image Modeling | ViT | Reconstruction loss |
| [[DF-DM (TNNLS 2023)|DF-DM]] | TNNLS 2023 | Self; Pretext task | DeepPixBiS, SSDG-R,  CDCN | GAN loss, Interpolation-based Consistency loss |
| [[MCAE (2023)|MCAE]] | 2023 | Self+Supervised; Masked Image Modeling | ViT | Reconstruction loss + Supervised Contrastive loss |
| [[AMA+M2A2E (2023)|AMA+M2A2E]] | 2023 | Self; Masked Image Modeling | ViT | Reconstruction loss |




<a name="CL" />

#### Continual learning


| Method    | Year | Replay or not | Backbone |  Loss |
| --------   | -----    | -----  |  -----  | -----  | 
| [[CM-PAD (IJCB 2020)|CM-PAD]] | IJCB 2020 | with Replay | DepthNet | batch/overall meta loss |
| [[Experience Replay (ICCV 2021)|Experience Replay]] | ICCV 2021 | with Replay | ResNet50 | BCE loss for identified novel and replayed samples |
| [[DCDCA+PPCR (2023)|DCDCA+PPCR]] | 2023 | Rehearsal-Free | ViT | BCE loss, Proxy Prototype Contrastive Regularization |



---
<a name="methods_advanced" />

### 3️⃣ Deep FAS methods with advanced sensor


<a name="sensor" />

#### Learning upon specialized sensor


| Method    | Year | Backbone | Loss |  Input | Static/Dynamic |
| --------   | -----    | -----  |  -----  | -----  | -----  |
| [[Thermal-FaceCNN (2019)|Thermal-FaceCNN]] | 2019 | AlexNet | Regression loss | Thermal infrared face image | S |
| [[SLNet (2019)|SLNet]] | 2019 | 17-layer CNN | Binary CE loss | Stereo (left&right) face images | S |
| [[Aurora-Guard (2019)|Aurora-Guard]] | 2019 | U-Net | Binary CE loss, Depth regression, Light Regression | Casted face with dynamic changing light specified by random light CAPTCHA | D |
| [[LFC (2019)|LFC]] | 2019 | AlexNet | Binary CE loss | Ray difference/microlens images from light field camera | S |
| [[PAAS (2020)|PAAS]] | 2020 | MobileNetV2 | Contrastive loss, SVM | Four-directional polarized face image | S |
| [[Face-Revelio (2020)|Face-Revelio]] | 2020 | Siamese-AlexNet | L1 distance | Four flash lights displayed on four quarters of a screen | D |
| [[SpecDiff (2020)|SpecDiff]] | 2020 | ResNet4 | Binary CE loss | Concatenated face images w/ and w/o flash | S |
| [[MC-PixBiS (2020)|MC-PixBiS]] | 2020 | DenseNet161 | Binary mask loss | SWIR images differences | S |
| [[Thermalization (2020)|Thermalization]] | 2020 | YOLO V3+GoogLeNet | Binary CE loss | Thermal infrared face image | S |
| [[DP Bin-Cls-Net (2021)|DP Bin-Cls-Net]] | 2021 | Shallow U-Net + Xception | Transformation consistency, Relative disparity loss, Binary CE loss | DP image pair | S |





<a name="multimodal" />

#### Multi-modal learning

| Method    | Year | Backbone | Loss |  Input | Fusion |
| --------   | -----    | -----  |  -----  | -----  | -----  |
| [[FaceBagNet (2019)|FaceBagNet]] | 2019 | Multi-stream CNN | Binary CE loss | RGB, Depth, NIR face patches | Feature-level |
| [[FeatherNets (2019)|FeatherNets]] | 2019 | Ensemble-FeatherNet | Binary CE loss | Depth, NIR | Decision-level |
| [[Attention (2019)|Attention]] | 2019 | ResNet18 | Binary CE loss, Center loss | RGB, Depth, NIR | Feature-level |
| [[mmfCNN (ACMMM 2019)|mmfCNN]] | ACMMM 2019 | ResNet34 | Binary CE loss, Binary Center Loss | RGB, NIR, Depth, HSV, YCbCr | Feature-level |
| [[MM-FAS (2019)|MM-FAS]] | 2019 | ResNet18/50 | Binary CE loss | RGB, NIR, Depth | Feature-level |
| [[AEs+MLP (2019)|AEs+MLP]] | 2019 | Autoencoder, MLP | Binary CE loss, Reconstruction loss | Grayscale-Depth-Infrared composition | Input-level |
| [[SD-Net (2019)|SD-Net]] | 2019 | ResNet18 | Binary CE loss | RGB, NIR, Depth | Feature-level |
| [[Dual-modal (2019)|Dual-modal]] | 2019 | MoblienetV3 | Binary CE loss | RGB, IR | Feature-level |
| [[Parallel-CNN (2020)|Parallel-CNN]] | 2020 | Attentional CNN | Binary CE loss | Depth, NIR | Feature-level |
| [[Multi-Channel Detector (2020)|Multi-Channel Detector]] | 2020 | RetinaNet (FPN+ResNet18) | Landmark regression, Focal loss | Grayscale-Depth-Infrared composition | Input-level |
| [[PSMM-Net (2020)|PSMM-Net]] | 2020 | ResNet18 | Binary CE loss for each stream | RGB, Depth, NIR | Feature-level |
| [[PipeNet (2020)|PipeNet]] | 2020 | SENet154 | Binary CE loss | RGB, Depth, NIR face patches | Feature-level |
| [[MM-CDCN (2020)|MM-CDCN]] | 2020 | CDCN | Pixel-wise binary loss, Contrastive depth loss | RGB, Depth, NIR | Feature&Decision-level |
| [[HGCNN (2020)|HGCNN]] | 2020 | Hypergraph-CNN, MLP | Binary CE loss | RGB, Depth | Feature-level |
| [[MCT-GAN (2020)|MCT-GAN]] | 2020 | CycleGAN, ResNet50 | GAN loss, Binary CE loss | RGB, NIR | Input-level |
| [[D-M-Net (2021)|D-M-Net]] | 2021 | ResNeXt | Binary CE loss | Multi-preprocessed Depth, RGB-NIR composition | Input&Feature-level |
| [[MA-Net (TIFS 2021)|MA-Net]] | TIFS 2021 | CycleGAN, ResNet18 | Binary CE loss, GAN loss | RGB, NIR | Feature-level |
| [[AMT (TMM 2021)|AMT]] | TMM 2021 | Translator: shallow encoder+decoder + ResNet; Discriminator: DenseNet | BCE loss, Pixel-wise binary loss, reconstruction loss | illumination normalized RGB or NIR or thermal or Depth | Input-level |
| [[CompreEval (2022)|CompreEval]] | 2022 | DenseNet-161 | BCE loss, Pixel-wise binary loss | RGB, Depth, NIR, SWIR, Thermal | Input-level |
| [[Conv-MLP (TIFS 2022)|Conv-MLP]] | TIFS 2022 | Conv-MLP | Binary CE Loss, Moat Loss | RGB, Depth, NIR | Input-level |
| [[Echo-FAS (TIFS 2022)|Echo-FAS]] | TIFS 2022 | ResNet18, Transformer | Binary CE Loss | RGB, Vocal | Feature-level |
| [[AMA+M2A2E (2023)|AMA+M2A2E]] | 2023 | ViT | BCE Loss, reconstruction loss for MAE | RGB, Depth, IR | Feature-level |
| [[SNM (TIFS 2023)|SNM]] | TIFS 2023 | ResNet18 | BCE Loss, center loss, cosine loss | Depth, IR | Feature-level |


<a name="flexmodal" />

#### Flexible-modal learning

| Method    | Year | Backbone | Loss |  Input | Fusion |
| --------   | -----    | -----  |  -----  | -----  | -----  |
| [[CMFL (CVPR 2021)|CMFL]] | CVPR 2021 | DenseNet161 | Binary CE loss, Cross modal focal loss | RGB, Depth | Feature-level |
| [[MA-ViT (IJCAI 2022)|MA-ViT]] | IJCAI 2022 | ViT-S/16 | Binary CE Loss on image and modality | RGB, Depth, NIR | Input&Feature-level |
| [[FlexModal-FAS (CVPRW 2023)|FlexModal-FAS]] | CVPRW 2023 | CDCN, ResNet50, ViT | BCE loss, Pixel-wise binary loss | RGB, Depth, IR | Feature-level |
| [[FM-ViT (TIFS 2023)|FM-ViT]] | TIFS 2023 | ViT | BCE loss for flexible-modal classification heads | RGB, Depth, IR | Feature-level |

