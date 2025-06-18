# Online LaTeX Compilation Options

## Option 1: Overleaf (Recommended)
1. Go to https://www.overleaf.com
2. Create a free account
3. Create a new project
4. Upload your presentation_aircraft_analysis.tex file
5. Upload all images from the ../images/ directory
6. Compile online

## Option 2: TeXLive.net
1. Go to https://texlive.net
2. Paste your LaTeX code
3. Upload images (may require adjusting image paths)
4. Compile online

## Option 3: ShareLaTeX
1. Go to https://www.sharelatex.com (now part of Overleaf)
2. Similar process to Overleaf

## Steps for Overleaf:
1. Create new project → "Upload Project"
2. Create a ZIP file containing:
   - presentation_aircraft_analysis.tex
   - All files from ../images/ directory
3. Upload and extract
4. Adjust image paths if needed (remove ../ prefix)
5. Compile

## Image Path Adjustments for Online:
If uploading to online service, you may need to change:
```latex
\includegraphics[width=0.87\textwidth]{../images/missingValues.png}
```
To:
```latex
\includegraphics[width=0.87\textwidth]{missingValues.png}
```

## Files to Include in ZIP:
- presentation_aircraft_analysis.tex
- Features-LOG-Distributions.png
- FeaturesDistributions.png
- Heatmap.png
- Lasso.png
- LassoFeatureSelection.png
- RegressionResiduals.png
- RegressionResidualsFitted.png
- ResidualsRIDGELASSO.png
- Ridge.png
- RidgeCV.png
- TargetComparison-LOG.png
- missingValues.png
