# Model Overview

## Proposed Framework
The manuscript describes a Graph Attention Network–Gaussian Process Regression–Coati Optimization Algorithm (GAT–GPR–COA) framework for predicting the properties of sustainable concrete incorporating polyethylene terephthalate (PET) and rice husk ash (RHA).

## Model Components
1. **Graph construction:** Represents concrete mixture constituents as nodes and their relationships as edges.
2. **Conditional Variational Autoencoder (CVAE):** Generates synthetic training observations from the training data.
3. **Graph Attention Network (GAT):** Learns representations of relationships among mixture constituents.
4. **Gaussian Process Regression (GPR):** Produces predictions using learned graph representations.
5. **Coati Optimization Algorithm (COA):** Searches for suitable model hyperparameters.
6. **Integrated Gradients:** Examines model-attributed contributions of mixture constituents.

## Experimental Data
The repository includes ten experimental mixtures (M0–M9). The uploaded CSV contains mixture proportions and the measured values for compressive strength, splitting tensile strength, flexural strength, and water absorption.

## Validation
The manuscript describes leave-one-mix-out validation. In each fold, one real mixture is held out for evaluation, and the other nine mixtures are used for model development.

## Implementation Status
This file describes the proposed methodology. It is not executable source code, and the model's computational results have not been independently reproduced from this repository.
