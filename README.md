# joefuqua.art

Art portfolio site — Joe Fuqua.

## Stack
- Astro (static site)
- Hosted on Cloudflare Pages
- Domain: joefuqua.art

## Local dev
```bash
npm install
npm run dev
```

## First push
```bash
git init
git branch -M main
git remote add origin git@github.com:YOUR-USER/YOUR-REPO.git
npm install
git add .
git commit -m "Initial site"
git push -u origin main
```

If you use HTTPS for GitHub instead of SSH, swap the remote URL accordingly.

## Cloudflare Pages
Create a Pages project connected to this GitHub repo with:

- Framework preset: `Astro`
- Build command: `npm run build`
- Build output directory: `dist`
- Node.js version: `20` or newer

After the first deployment succeeds, attach the custom domain `joefuqua.art` in Cloudflare.

## Adding new artwork

### 1. Prepare the image
- Resize to max 1200px on the long edge
- Export as JPG, quality 80-85
- Name it with a slug: `my-new-piece.jpg`

### 2. Place the image
Drop it in the right folder under `public/images/`:
```
public/images/watercolor/
public/images/digital/
public/images/multimedia/
public/images/ai/
```

### 3. Add to catalog
Open `src/data/catalog.ts` and add an entry:
```ts
{
  slug: 'my-new-piece',        // matches filename without .jpg
  title: 'My New Piece',
  year: '2025',
  collection: 'watercolor',    // watercolor | digital | multimedia | ai
  medium: 'Watercolor on paper',
  desc: 'One or two sentences about the piece.',
  available: true,             // true = show inquiry button
},
```

### 4. Push
```bash
git add .
git commit -m "Add: My New Piece"
git push
```
Cloudflare Pages rebuilds automatically after the push.

## Image resize script
Run this to batch-resize a folder of images before adding them:
```bash
python3 scripts/resize.py /path/to/your/images watercolor
```
Output goes to `public/images/[collection]/`.
