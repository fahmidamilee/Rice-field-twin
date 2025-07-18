
# 🚀 Deployment Guide for Rice Field Digital Twin

## ☁️ Hosting on Render.com (or Hugging Face Spaces)

### 1. Upload to GitHub
- Create a new repo: https://github.com/new
- Upload the extracted files from the ZIP manually, or use:

```bash
git init
git remote add origin https://github.com/your_username/rice-field-twin.git
git add .
git commit -m "Initial commit"
git push -u origin master
```

### 2. Render Deployment (Docker)
- Go to: https://render.com/
- Click **New Web Service**
- Connect your GitHub repo
- Choose:
  - **Environment**: Docker
  - **Port**: 8050
- Click **Deploy**. Wait 1–2 mins. Your app is live!

---

## 📱 Tauri App: Build for Android & iOS

Tauri support for mobile is experimental, but here’s how to start.

### Step 1: Prerequisites
- Install Rust: https://rustup.rs
- Install Node.js + npm: https://nodejs.org
- Install Tauri CLI:
```bash
cargo install tauri-cli
```

### Step 2: Add Android/iOS Targets

**Android**
```bash
rustup target add aarch64-linux-android
```

Install NDK/SDK via Android Studio → Preferences → SDK Tools → Check "NDK"

**iOS (macOS only)**
```bash
rustup target add aarch64-apple-ios
```

---

### Step 3: Build Mobile App

From your Tauri app folder:

```bash
pnpm install
pnpm tauri build --target aarch64-linux-android
```

For iOS:
```bash
pnpm tauri build --target aarch64-apple-ios
```

Generated APKs or iOS .app/.ipa files will be inside `src-tauri/target/`.

---

## ✅ Tips
- Mobile builds may require config changes in `tauri.conf.json`
- Webview must point to hosted live app (not localhost)
  - e.g. `"https://your-rice-twin.onrender.com"`

