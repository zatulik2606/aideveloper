#!/bin/bash

# GitHub Pages Deployment Script

echo "🚀 Starting GitHub Pages deployment..."

# Create public directory if it doesn't exist
mkdir -p public

# Copy all static files to public directory
cp index.html public/ 2>/dev/null || touch public/index.html
cp styles.css public/ 2>/dev/null || touch public/styles.css  
cp script.js public/ 2>/dev/null || touch public/script.js
cp .nojekyll public/ 2>/dev/null || touch public/.nojekyll

# Navigate to public directory
cd public

# Initialize git if not already initialized
if [ ! -d ".git" ]; then
    git init
    git remote add origin https://github.com/zatulik2606/aideveloper.git
fi

# Add files
git add .

# Commit if there are changes
if ! git diff --staged --quiet; then
    git commit -m "Deploy to GitHub Pages - $(date)"
    
    # Force push to main branch
    git push -f origin main:gh-pages
    
    echo "✅ Successfully deployed to GitHub Pages!"
    echo "🔗 Your site should be available at: https://zatulik2606.github.io/aideveloper"
else
    echo "ℹ️ No changes to deploy"
fi

cd ..