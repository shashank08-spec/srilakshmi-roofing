# Deploying to Render — Step by Step

This guide puts your website online at a free, shareable web address so you
can check it on your phone and send it to others for feedback.

Total time: about 15 minutes.

---

## Before You Start — Two Things to Know

**1. The free website sleeps when nobody visits.**
After 15 minutes with no visitors, Render puts a free site to sleep. The
next person to open it waits about a minute for it to wake up. Every visit
after that is instant. This is completely fine for checking and sharing —
but before you advertise the site to real customers, upgrade to Render's
paid plan (around $7/month) so it's always awake and instant.

**2. The free database is deleted after 30 days.**
Render deletes free PostgreSQL databases 30 days after they're created
(you get a 14-day warning period to upgrade first). For checking the site,
that's fine. But **do not collect real customer enquiries on the free
database** — you'd lose them. Upgrade the database to a paid plan before
you start sending real customers to the site.

Neither of these affects how the site looks or works while you're testing.

---

## Step 1 — Put the Project on GitHub

You said you already have a GitHub account, so:

1. Go to https://github.com/new
2. **Repository name:** `srilakshmi-roofing`
3. Choose **Private** (recommended — nobody needs to see the code)
4. Do **not** tick "Add a README file" — the project already has one
5. Click **Create repository**

Now upload the project. The easiest way without commands:

1. On the new empty repository page, click **"uploading an existing file"**
2. Open your `srilakshmi` folder on your computer
3. Select everything inside it — including the `static` and `templates`
   folders — and drag it all into the browser window
4. Wait for all files to finish uploading (you should see `app.py`,
   `render.yaml`, and the `static` and `templates` folders listed)
5. Click **Commit changes**

> **Important:** make sure the `static` and `templates` folders uploaded.
> Without them the site will deploy but every page will show an error.

If you prefer the command line instead, from inside the `srilakshmi` folder:

```bash
git init
git add .
git commit -m "Initial commit — Sri Lakshmi Roofing Industry website"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/srilakshmi-roofing.git
git push -u origin main
```

---

## Step 2 — Deploy on Render

1. Go to https://render.com and sign up — choose **"Sign in with GitHub"**,
   which saves you connecting the accounts later
2. In the dashboard click **New +** → **Blueprint**
3. Find and select your `srilakshmi-roofing` repository
   (if it doesn't appear, click **Configure account** and give Render
   access to the repository)
4. Render reads the included `render.yaml` file and shows you what it will
   create: a **web service** and a **PostgreSQL database**
5. Give the blueprint a name (`srilakshmi-roofing` is fine)
6. Click **Apply**

Render now builds the site. The first build takes roughly 3–5 minutes —
you can watch the log scroll by. When it finishes you'll see a green
**Live** badge and a web address like:

```
https://srilakshmi-roofing.onrender.com
```

That's your website. Open it on your phone, send it to anyone.

Everything is already wired up: the database connects automatically, and a
secure secret key is generated for you. There are no passwords to copy.

---

## Step 3 — Check It Works

Open the site and walk through:

- Every page loads from the menu (Home, About, Products, Brands, Why Choose
  Us, Gallery, FAQ, Contact)
- The **Call** and **WhatsApp** floating buttons work on your phone
- The **Request a Quote** form submits and shows a green success message
- The Google Map appears on the Contact page
- It looks right on your phone, not just your computer

If the quote form shows a success message, the database is working.

---

## Updating the Site Later

Any change you push to GitHub deploys automatically within a few minutes.
To change wording, prices or products, edit **`data.py`**; to change phone
numbers, address or business hours, edit **`config.py`**. Commit the change
to GitHub and Render redeploys on its own.

---

## When You're Ready for Real Customers

Before pointing real customers or Google at the site:

1. **Upgrade both the web service and the database** to a paid plan
   (about $7/month each) — this stops the sleeping and, critically, stops
   the database being deleted with your enquiries in it.
2. **Buy your domain** (for example `srilakshmiroofing.in` — around
   ₹800–1,200/year from GoDaddy, Hostinger or Namecheap) and connect it in
   Render under **Settings → Custom Domains**. Render provides the HTTPS
   certificate free.
3. **Update `SITE_DOMAIN`** in `render.yaml` (or in Render's environment
   variables) to your real domain, so the SEO tags and sitemap point to the
   right place.
4. **Add your real photographs** to the hero section, product cards and
   gallery — this makes the single biggest difference to how trustworthy
   the site feels.
5. **Set up Google Business Profile** with exactly the same name, address
   and phone number shown on the Contact page. For a local business like
   yours this affects Google rankings more than anything on the website
   itself.
6. **Submit your sitemap** at `yourdomain.com/sitemap.xml` to Google Search
   Console.

---

## If Something Goes Wrong

**Build fails with a `psycopg2` error** — Render used the wrong Python
version. In your service go to **Environment** and confirm
`PYTHON_VERSION` is set to `3.11.9`, then click **Manual Deploy**.

**Every page shows "TemplateNotFound"** — the `templates` folder didn't
upload to GitHub. Check your repository; if it's missing, upload it.

**The site shows no styling, just plain text** — the `static` folder didn't
upload. Same fix.

**First visit is very slow** — that's the free tier waking up. Normal.
Wait about a minute.

**Forms show an error message with your phone number** — the database
isn't connected. Check in Render that the database was created and shows
status **Available**.
