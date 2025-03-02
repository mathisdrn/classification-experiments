---
title: Multi-dimensional Scaling
---

### Main Concept

Multi-Dimensional Scaling (MDS) aims to find a low-dimensional representation of data based on a matrix of pairwise dissimilarities (or distances). Unlike methods that operate directly on the data points themselves, MDS works with a dissimilarity matrix that encodes the relationships between data points. The core idea is to find a configuration of points in a lower-dimensional space such that the distances between these points closely match the given dissimilarities. MDS transforms the original data representation by creating a new set of coordinates in a lower-dimensional space. The coordinates of data points change as they are positioned in this new space to reflect the input dissimilarities.

### Theoretical Aspect

There are two main types of MDS: Classical MDS (also known as Principal Coordinates Analysis) and Metric/Non-metric MDS.

*   **Classical MDS:**

    Classical MDS aims to preserve the Euclidean distances between points. Given a matrix of squared distances $\mathbf{D}^{(2)}$ (where $D_{ij}^{(2)} = ||\mathbf{x}_i - \mathbf{x}_j||^2$), the goal is to find a configuration of points $\mathbf{X}$ in a lower-dimensional space such that the squared Euclidean distances between these points are as close as possible to $\mathbf{D}^{(2)}$. The key idea is to use double centering and eigenvalue decomposition.

*   **Metric/Non-metric MDS:**

    Metric MDS generalizes classical MDS by allowing the input to be any dissimilarity matrix, not necessarily derived from Euclidean distances. It minimizes a *stress* function that measures the discrepancy between the input dissimilarities $\delta_{ij}$ and the distances $d_{ij}$ in the low-dimensional space. A common stress function is Kruskal's stress:

    $Stress = \sqrt{\frac{\sum_{i<j} (d_{ij} - \hat{d}_{ij})^2}{\sum_{i<j} d_{ij}^2}}$

    where $d_{ij} = ||\mathbf{y}_i - \mathbf{y}_j||$ are the distances in the low-dimensional space, and $\hat{d}_{ij}$ are the *disparities*, which are monotonic transformations of the dissimilarities $\delta_{ij}$. In metric MDS, $\hat{d}_{ij} = \delta_{ij}$. In non-metric MDS, the $\hat{d}_{ij}$ are chosen to be monotonic with the $\delta_{ij}$ but not necessarily equal.

    The key variables being optimized in both Metric and Non-metric MDS is $\mathbf{Y}$, the matrix of low-dimensional embeddings.

### Solution Methodology

*   **Classical MDS:**

    1.  **Double Centering:** Compute the matrix $\mathbf{B} = -\frac{1}{2} \mathbf{J} \mathbf{D}^{(2)} \mathbf{J}$, where $\mathbf{J} = \mathbf{I} - \frac{1}{n}\mathbf{1}\mathbf{1}^T$ is the centering matrix.
    2.  **Eigenvalue Decomposition:** Perform eigenvalue decomposition of $\mathbf{B}$: $\mathbf{B} = \mathbf{V} \mathbf{\Lambda} \mathbf{V}^T$.
    3.  **Embedding:** The low-dimensional embedding $\mathbf{Y}$ is given by $\mathbf{Y} = \mathbf{\Lambda}_k^{1/2} \mathbf{V}_k^T$, where $\mathbf{\Lambda}_k$ contains the $k$ largest eigenvalues and $\mathbf{V}_k$ contains the corresponding eigenvectors.

*   **Metric/Non-metric MDS:**

    1.  **Initialization:** Initialize a configuration of points $\mathbf{Y}$ in the low-dimensional space (e.g., randomly or using classical MDS).
    2.  **Disparity Computation (Non-metric MDS):** Find disparities $\hat{d}_{ij}$ that are monotonic with the dissimilarities $\delta_{ij}$.
    3.  **Stress Minimization:** Minimize the stress function using an iterative optimization procedure, such as majorization, gradient descent or SMACOF (Scaling by MAjorizing a COmplicated Function).
    4.  **Iteration:** Repeat steps 2 and 3 until convergence.

The solution involves standard numerical methods like matrix operations, eigenvalue decomposition, and iterative optimization algorithms.

### Global Optimality

*   **Classical MDS:** Classical MDS provides a closed-form solution that is optimal in the sense that it minimizes the squared difference between the squared distances in the low-dimensional space and the input squared distances. It is a globally optimal solution under the assumption that the input dissimilarities are Euclidean distances.

*   **Metric/Non-metric MDS:** The iterative optimization procedures used in metric and non-metric MDS do not guarantee finding a global minimum of the stress function. The optimization can get stuck in local minima. The quality of the solution depends on the initialization and the choice of optimization algorithm. Multiple restarts with different initializations are often used to try to find a better solution.

Key limitations of include:
- Sensitivity to noise in distance measurements: MDS relies on accurate pairwise distances. Noise or errors in these distances can significantly distort the resulting embedding.
- Difficulty with non-Euclidean manifolds: MDS assumes that the data can be embedded in a Euclidean space while preserving distances. If the underlying manifold has a significantly different geometry, MDS may struggle.
- Computational complexity of at least $O(n^2)$ for MDS and potentially higher for iterative methods: This makes it computationally expensive for very large datasets.
- Potential for local minima in iterative MDS: Iterative MDS methods use optimization algorithms that can get stuck in local minima, leading to suboptimal embeddings.

### Conclusion

Multi-Dimensional Scaling is a versatile technique for dimensionality reduction that works with dissimilarity data. Classical MDS provides a closed-form solution for Euclidean distances, while metric and non-metric MDS offer more flexibility for general dissimilarity measures but rely on iterative optimization. A meaningful use case is in sensory analysis, where panelists provide dissimilarity ratings between different products (e.g., wines, cheeses). MDS can then be used to create a perceptual map that visualizes the relationships between the products based on the panelist's judgments.
