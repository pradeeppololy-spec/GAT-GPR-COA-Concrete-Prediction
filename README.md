# GAT–GPR–COA for PET–RHA Concrete Prediction

## Overview
This repository accompanies research on predicting the mechanical and durability properties of sustainable concrete incorporating recycled polyethylene terephthalate (PET) and rice husk ash (RHA).

## Experimental Dataset
The file `experimental_data_M0-M9_complete.csv` contains data for ten concrete mixtures (M0–M9), including mixture proportions and six target properties: compressive strength (CS), splitting tensile strength (STS), flexural strength (FS), water absorption (WA), modulus of elasticity (MoE), and rapid chloride permeability (RCPT).

## Repository Contents
- `experimental_data_M0-M9_complete.csv` — experimental dataset.
- `main.py` — dataset-loading and column-checking script.
- `validate_data.py` — dataset validation script.
- `requirements.txt` — Python package dependencies.
- `MODEL_OVERVIEW.md` — description of the proposed modelling approach.
- `REPRODUCIBILITY.md` — reproducibility information and limitations.
- `HOW_TO_RUN.md` — instructions for checking the dataset.
- `DATA_AVAILABILITY.md` — data availability statement.
- `Algorithm 1 End-to-End GAT-GPR-COA.txt` — algorithm description.

## Validation
The manuscript describes leave-one-mix-out (LOMO) validation, with synthetic augmentation restricted to the training fold. The scripts currently provided do not implement this complete modelling and validation pipeline.

## Current Status
The repository currently provides the experimental dataset and preliminary data-checking scripts. The complete GAT–GPR–COA implementation and independent reproduction of the reported predictive results remain to be completed.

## Citation
Please cite the associated research article when using this dataset or methodology. Add the final publication citation and DOI here.
