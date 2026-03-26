# Bastusastra - Complete Project Plan

## Project Overview
A comprehensive Vedic astrology web application for generating birth charts (Kundali), calculating Muhurtas (auspicious times), matching horoscopes for marriage, and providing daily/weekly/monthly/yearly horoscopes.

**Tech Stack:**
- **Frontend:** Next.js 14+ with TypeScript, Tailwind CSS, shadcn/ui
- **Backend:** Node.js with Express/Fastify or Python with FastAPI
- **Astro Engine:** Pure TypeScript/Python calculation library
- **Database:** PostgreSQL
- **Deployment:** Vercel (frontend), Railway/Render (backend)

---

## Project Architecture

```
bastusastra/
├── frontend/                    # Next.js 14 Application
│   ├── app/                     # Next.js 14 App Router
│   │   ├── (marketing)/         # Marketing pages
│   │   │   ├── page.tsx         # Landing page
│   │   │   ├── about/
│   │   │   └── features/
│   │   ├── (auth)/              # Authentication pages
│   │   │   ├── login/
│   │   │   ├── register/
│   │   │   └── forgot-password/
│   │   ├── dashboard/           # User dashboard
│   │   ├── kundali/             # Birth chart features
│   │   │   ├── new/
│   │   │   ├── [id]/
│   │   │   └── list/
│   │   ├── panchang/            # Daily Panchang
│   │   ├── muhurta/             # Auspicious time finder
│   │   ├── matching/            # Horoscope matching
│   │   ├── horoscope/           # Daily/weekly horoscopes
│   │   └── api/                 # API routes
│   ├── components/              # React components
│   │   ├── ui/                  # shadcn/ui components
│   │   ├── charts/              # Chart display components
│   │   ├── forms/               # Form components
│   │   └── layout/              # Layout components
│   ├── lib/                     # Utility functions
│   ├── hooks/                   # Custom React hooks
│   ├── types/                   # TypeScript types
│   └── public/                  # Static assets
│
├── backend/                     # API Server
│   ├── src/
│   │   ├── controllers/         # Route controllers
│   │   ├── services/            # Business logic
│   │   ├── models/              # Database models
│   │   ├── middleware/          # Express middleware
│   │   ├── routes/              # API routes
│   │   ├── utils/               # Utility functions
│   │   └── config/              # Configuration
│   ├── tests/                   # Test files
│   └── package.json
│
├── astro-engine/                # Astrology Calculation Library
│   ├── src/
│   │   ├── core/                # Core calculations
│   │   │   ├── ayanamsa.ts      # Ayanamsa calculations
│   │   │   ├── planets.ts       # Planetary positions
│   │   │   ├── houses.ts        # House calculations
│   │   │   └── time.ts          # Time conversions
│   │   ├── charts/              # Chart calculations
│   │   │   ├── kundali.ts       # Birth chart
│   │   │   ├── divisional.ts    # Varga charts
│   │   │   └── panchang.ts      # Panchang
│   │   ├── dasha/               # Dasha systems
│   │   │   ├── vimshottari.ts
│   │   │   └── yogini.ts
│   │   ├── analysis/            # Chart analysis
│   │   │   ├── yogas.ts         # Yoga detection
│   │   │   ├── doshas.ts        # Dosha detection
│   │   │   └── predictions.ts   # Prediction engine
│   │   ├── matching/            # Compatibility
│   │   │   └── ashta-koota.ts
│   │   └── muhurta/             # Electional astrology
│   │       └── choghadiya.ts
│   ├── tests/                   # Unit tests
│   └── package.json
│
├── database/                    # Database Schema & Migrations
│   ├── migrations/
│   ├── seeds/
│   └── schema.sql
│
├── docs/                        # Documentation
│   ├── knowledge-base.md        # Extracted book knowledge
│   ├── algorithms.md            # Calculation algorithms
│   ├── gaps.md                  # Knowledge gaps
│   ├── PROJECT_PLAN.md          # This file
│   └── api/                     # API documentation
│
├── docker-compose.yml           # Local development setup
├── .env.example                 # Environment variables template
├── .gitignore
└── README.md
```

---

## Complete TODO List by Phase

### ✅ PHASE 0: Knowledge Extraction (COMPLETED)
- [x] Read and extract from "Predictive Astrology of the Hindus" (358 pages)
- [x] Read and extract from "Jataka Parijata Vol 1" (324 pages)
- [ ] Read and extract from "Brihat Jataka" (588 pages - needs OCR)
- [x] Create comprehensive knowledge-base.md
- [x] Create algorithms.md with pseudo-code
- [x] Document gaps in gaps.md
- [x] Initialize Git repository and push initial commit

---

### 🔄 PHASE 1: Project Skeleton & Setup

#### Job 1.1: Repository Setup
- [ ] Create project directory structure
- [ ] Set up monorepo configuration (optional: Turborepo)
- [ ] Configure GitHub Actions CI/CD
- [ ] Set up ESLint and Prettier
- [ ] Configure pre-commit hooks

#### Job 1.2: Frontend Setup
- [ ] Initialize Next.js 14 with TypeScript
- [ ] Configure Tailwind CSS
- [ ] Install shadcn/ui components
- [ ] Set up dark/light mode
- [ ] Configure fonts (Inter for UI, Noto Sans Devanagari for Hindi)
- [ ] Set up internationalization (i18n) for Hindi/English
- [ ] Create base layout components

#### Job 1.3: Backend Setup
- [ ] Initialize Node.js/Express or Python/FastAPI project
- [ ] Set up TypeScript (if Node.js)
- [ ] Configure environment variables
- [ ] Set up error handling middleware
- [ ] Configure CORS
- [ ] Set up logging (Winston/Pino)

#### Job 1.4: Database Setup
- [ ] Create PostgreSQL schema
- [ ] Set up database migrations (Knex/Prisma)
- [ ] Create seed data for reference tables
- [ ] Configure connection pooling
- [ ] Set up database backups

#### Job 1.5: Docker & Dev Environment
- [ ] Create docker-compose.yml
- [ ] Configure PostgreSQL container
- [ ] Configure Redis container (for caching)
- [ ] Configure backend container
- [ ] Create development startup scripts
- [ ] Document setup instructions

#### Job 1.6: Astro Engine Setup
- [ ] Initialize calculation library
- [ ] Set up unit testing framework (Jest/Vitest)
- [ ] Create basic calculation utilities
- [ ] Set up Swiss Ephemeris integration
- [ ] Create validation functions

**Commit Point:** `feat(phase1): Complete project setup with all services`

---

### 🔄 PHASE 2: Astro Engine - Core Calculations

#### Job 2.1: Foundational Astronomy
- [ ] Implement Julian Day Number calculator
- [ ] Implement Ayanamsa calculator (Lahiri)
- [ ] Implement sidereal time calculator
- [ ] Implement sunrise/sunset calculator
- [ ] Implement Local Mean Time converter
- [ ] Write unit tests for all functions

**Functions:**
- `calculateJDN(date, time)`
- `calculateAyanamsa(julianDay)`
- `calculateSiderealTime(julianDay, longitude)`
- `calculateSunriseSunset(date, latitude, longitude)`
- `convertStandardToLMT(standardTime, longitude)`

#### Job 2.2: Planetary Position Engine
- [ ] Integrate Swiss Ephemeris library
- [ ] Implement Sun position calculator
- [ ] Implement Moon position calculator
- [ ] Implement Mercury, Venus, Mars positions
- [ ] Implement Jupiter, Saturn positions
- [ ] Implement Rahu/Ketu (mean node) calculator
- [ ] Implement retrogression detection
- [ ] Write unit tests

**Functions:**
- `getPlanetPosition(planet, julianDay)`
- `getAllPlanetPositions(julianDay)`
- `isRetrograde(planet, julianDay)`
- `calculateRahuKetu(julianDay)`

#### Job 2.3: Ascendant & House Calculations
- [ ] Implement ascendant calculator
- [ ] Implement Equal House system
- [ ] Implement Placidus House system
- [ ] Implement Sripati House system (optional)
- [ ] Implement house lord calculator
- [ ] Write unit tests

**Functions:**
- `calculateAscendant(julianDay, latitude, longitude)`
- `calculateEqualHouses(ascendant)`
- `calculatePlacidusHouses(julianDay, latitude, longitude)`
- `getHouseLord(houseNumber, ascendantSign)`

#### Job 2.4: Nakshatra & Panchang Elements
- [ ] Implement Nakshatra finder
- [ ] Implement Tithi calculator
- [ ] Implement Karana calculator
- [ ] Implement Yoga calculator
- [ ] Implement Hora calculator
- [ ] Write unit tests

**Functions:**
- `findNakshatra(moonLongitude)`
- `calculateTithi(sunLong, moonLong)`
- `calculateKarana(tithiNumber, fraction)`
- `calculateYoga(sunLong, moonLong)`
- `calculateHora(time, dayOfWeek)`

#### Job 2.5: Divisional Charts (Vargas)
- [ ] Implement Hora (D-2)
- [ ] Implement Drekkana (D-3)
- [ ] Implement Navamsa (D-9)
- [ ] Implement Dasamamsa (D-10)
- [ ] Implement Dwadasamsa (D-12)
- [ ] Implement Saptamamsa (D-7)
- [ ] Implement Trimsamsa (D-30)
- [ ] Implement Shodasamsa (D-16) and others
- [ ] Write unit tests

**Functions:**
- `calculateNavamsa(planetLongitude, sign)`
- `calculateDasamamsa(planetLongitude, sign)`
- `calculateAllVargas(planetPositions)`

**Commit Point:** `feat(phase2): Complete core astro calculations`

---

### 🔄 PHASE 3: Astro Engine - Advanced Features

#### Job 3.1: Birth Chart (Kundali) Generator
- [ ] Create Kundali data structure
- [ ] Implement complete chart calculation
- [ ] Implement chart saving/loading
- [ ] Write unit tests

**Functions:**
- `generateKundali(birthData)`
- `getChartPositions(kundali)`
- `serializeKundali(kundali)`
- `deserializeKundali(data)`

#### Job 3.2: Dasha Systems
- [ ] Implement Vimshottari Dasha calculation
- [ ] Implement Antardasha (Bhukti) calculation
- [ ] Implement Pratyantardasha calculation
- [ ] Implement Dasha balance at birth
- [ ] Implement Yogini Dasha (optional)
- [ ] Write unit tests

**Functions:**
- `calculateVimshottariDasha(moonLongitude, julianDay)`
- `calculateAntardasha(mahadashaLord, startDate)`
- `getCurrentDasha(dashaSequence, currentDate)`

#### Job 3.3: Yoga Detection Engine
- [ ] Implement Raj Yoga detection
- [ ] Implement Dhana Yoga detection
- [ ] Implement Gaja Kesari Yoga detection
- [ ] Implement Budha-Aditya Yoga detection
- [ ] Implement Chandra-Mangala Yoga detection
- [ ] Implement other major Yogas (20+)
- [ ] Write unit tests

**Functions:**
- `detectRajYoga(planetPositions, houses, ascendant)`
- `detectDhanaYoga(planetPositions, houses, ascendant)`
- `detectAllYogas(kundali)`

#### Job 3.4: Dosha Detection Engine
- [ ] Implement Mangal Dosha (Manglik) detection
- [ ] Implement Kaal Sarp Dosha detection
- [ ] Implement Pitru Dosha detection
- [ ] Implement Nadi Dosha detection
- [ ] Implement dosha cancellation rules
- [ ] Write unit tests

**Functions:**
- `detectMangalDosha(marsPosition, ascendant)`
- `detectKaalSarpDosha(planetPositions, rahu, ketu)`
- `checkDoshaCancellation(doshaType, chartData)`

#### Job 3.5: Panchang Generator
- [ ] Implement daily Panchang generator
- [ ] Implement Rahu Kaal calculator
- [ ] Implement Yamaganda calculator
- [ ] Implement Gulika calculator
- [ ] Implement Choghadiya calculator
- [ ] Implement monthly calendar generator
- [ ] Write unit tests

**Functions:**
- `generatePanchang(date, latitude, longitude)`
- `calculateRahuKaal(dayOfWeek, sunrise, sunset)`
- `calculateChoghadiya(sunrise, sunset, dayOfWeek)`

#### Job 3.6: Muhurta Engine
- [ ] Implement general Muhurta finder
- [ ] Implement Marriage Muhurta rules
- [ ] Implement Griha Pravesh Muhurta
- [ ] Implement Vehicle purchase Muhurta
- [ ] Implement business start Muhurta
- [ ] Write unit tests

**Functions:**
- `findAuspiciousMuhurta(dateRange, activity, location)`
- `checkMuhurtaCompatibility(date, activity, chartData)`

#### Job 3.7: Compatibility (Kundali Milan) Engine
- [ ] Implement Varna Koota (1 point)
- [ ] Implement Vashya Koota (2 points)
- [ ] Implement Tara Koota (3 points)
- [ ] Implement Yoni Koota (4 points)
- [ ] Implement Graha Maitri (5 points)
- [ ] Implement Gana Koota (6 points)
- [ ] Implement Bhakoot Koota (7 points)
- [ ] Implement Nadi Koota (8 points)
- [ ] Implement Mangal Dosha compatibility check
- [ ] Write unit tests

**Functions:**
- `calculateAshtaKoota(boyChart, girlChart)`
- `checkMangalDoshaCompatibility(boyChart, girlChart)`
- `getCompatibilityReport(matchResult)`

**Commit Point:** `feat(phase3): Complete advanced astro features`

---

### 🔄 PHASE 4: Backend API Development

#### Job 4.1: Authentication & User Management
- [ ] Implement user registration
- [ ] Implement user login (JWT)
- [ ] Implement password reset
- [ ] Implement email verification
- [ ] Implement OAuth (Google, Facebook)
- [ ] Create user profile endpoints
- [ ] Write API tests

**Endpoints:**
- `POST /api/auth/register`
- `POST /api/auth/login`
- `POST /api/auth/forgot-password`
- `POST /api/auth/reset-password`
- `GET /api/auth/me`
- `PUT /api/auth/profile`

#### Job 4.2: Kundali API
- [ ] Create Kundali generation endpoint
- [ ] Create Kundali retrieval endpoint
- [ ] Create Kundali update endpoint
- [ ] Create Kundali delete endpoint
- [ ] Create Kundali list endpoint
- [ ] Implement PDF export
- [ ] Write API tests

**Endpoints:**
- `POST /api/kundali/generate`
- `GET /api/kundali/:id`
- `PUT /api/kundali/:id`
- `DELETE /api/kundali/:id`
- `GET /api/kundali`
- `GET /api/kundali/:id/pdf`

#### Job 4.3: Panchang API
- [ ] Create daily Panchang endpoint
- [ ] Create monthly Panchang endpoint
- [ ] Create location-based Panchang endpoint
- [ ] Write API tests

**Endpoints:**
- `GET /api/panchang/daily`
- `GET /api/panchang/monthly`
- `GET /api/panchang/location/:city`

#### Job 4.4: Muhurta API
- [ ] Create Muhurta finder endpoint
- [ ] Create activity-specific Muhurta endpoints
- [ ] Write API tests

**Endpoints:**
- `POST /api/muhurta/find`
- `GET /api/muhurta/marriage`
- `GET /api/muhurta/griha-pravesh`
- `GET /api/muhurta/vehicle`

#### Job 4.5: Horoscope API
- [ ] Create daily horoscope endpoint
- [ ] Create weekly horoscope endpoint
- [ ] Create monthly horoscope endpoint
- [ ] Create yearly horoscope endpoint
- [ ] Write API tests

**Endpoints:**
- `GET /api/horoscope/daily/:rashi`
- `GET /api/horoscope/weekly/:rashi`
- `GET /api/horoscope/monthly/:rashi`
- `GET /api/horoscope/yearly/:rashi`

#### Job 4.6: Matching API
- [ ] Create Kundali matching endpoint
- [ ] Create detailed compatibility report endpoint
- [ ] Write API tests

**Endpoints:**
- `POST /api/matching/ashta-koota`
- `POST /api/matching/detailed-report`

#### Job 4.7: Dasha API
- [ ] Create Vimshottari Dasha endpoint
- [ ] Create current Dasha endpoint
- [ ] Create Dasha timeline endpoint
- [ ] Write API tests

**Endpoints:**
- `GET /api/dasha/vimshottari/:kundaliId`
- `GET /api/dasha/current/:kundaliId`
- `GET /api/dasha/timeline/:kundaliId`

#### Job 4.8: Common Services
- [ ] Implement rate limiting
- [ ] Implement request validation
- [ ] Implement error handling
- [ ] Implement caching (Redis)
- [ ] Implement logging
- [ ] Create API documentation (Swagger/OpenAPI)

**Commit Point:** `feat(phase4): Complete backend API`

---

### 🔄 PHASE 5: Frontend Development

#### Job 5.1: Landing Page & Marketing
- [ ] Create hero section
- [ ] Create features section
- [ ] Create testimonials section
- [ ] Create pricing section (if applicable)
- [ ] Create footer
- [ ] SEO optimization

#### Job 5.2: Authentication Pages
- [ ] Create login page
- [ ] Create registration page
- [ ] Create forgot password page
- [ ] Create password reset page
- [ ] Implement auth state management

#### Job 5.3: Dashboard
- [ ] Create dashboard layout
- [ ] Create saved charts widget
- [ ] Create daily Panchang widget
- [ ] Create daily horoscope widget
- [ ] Create recent activity widget

#### Job 5.4: Kundali Pages
- [ ] Create birth chart input form
- [ ] Create location autocomplete
- [ ] Create chart display (North Indian style)
- [ ] Create chart display (South Indian style)
- [ ] Create planet positions table
- [ ] Create house details view
- [ ] Create Dasha timeline view
- [ ] Create divisional charts tabs
- [ ] Create PDF export functionality
- [ ] Create share functionality

#### Job 5.5: Panchang Page
- [ ] Create daily Panchang display
- [ ] Create Choghadiya table
- [ ] Create Rahu Kaal display
- [ ] Create monthly calendar view
- [ ] Create festival listing

#### Job 5.6: Muhurta Pages
- [ ] Create activity selector
- [ ] Create date range picker
- [ ] Create location input
- [ ] Create results display
- [ ] Create detailed Muhurta view

#### Job 5.7: Matching Page
- [ ] Create two-person input form
- [ ] Create Ashta Koota results display
- [ ] Create detailed analysis view
- [ ] Create printable report

#### Job 5.8: Horoscope Pages
- [ ] Create Rashi selector
- [ ] Create daily horoscope view
- [ ] Create weekly horoscope view
- [ ] Create monthly horoscope view
- [ ] Create yearly horoscope view

#### Job 5.9: Common Components
- [ ] Create navigation
- [ ] Create sidebar
- [ ] Create loading states
- [ ] Create error boundaries
- [ ] Create toast notifications
- [ ] Create modal components
- [ ] Create form validation

#### Job 5.10: Responsive Design
- [ ] Mobile optimization
- [ ] Tablet optimization
- [ ] Print styles for charts

**Commit Point:** `feat(phase5): Complete frontend development`

---

### 🔄 PHASE 6: Integration & Testing

#### Job 6.1: Frontend-Backend Integration
- [ ] Connect authentication APIs
- [ ] Connect Kundali APIs
- [ ] Connect Panchang APIs
- [ ] Connect Muhurta APIs
- [ ] Connect Matching APIs
- [ ] Connect Horoscope APIs

#### Job 6.2: End-to-End Testing
- [ ] Write E2E tests for critical user flows
- [ ] Test chart generation
- [ ] Test Kundali matching
- [ ] Test Muhurta finder

#### Job 6.3: Performance Optimization
- [ ] Implement frontend caching
- [ ] Optimize images
- [ ] Implement lazy loading
- [ ] Optimize API response times
- [ ] Add database indexes

#### Job 6.4: Security Audit
- [ ] Review authentication flow
- [ ] Check for XSS vulnerabilities
- [ ] Check for CSRF vulnerabilities
- [ ] Implement input sanitization
- [ ] Secure API endpoints

**Commit Point:** `feat(phase6): Complete integration and testing`

---

### 🔄 PHASE 7: Polish & Production

#### Job 7.1: Multi-language Support
- [ ] Implement Hindi translations
- [ ] Implement English translations
- [ ] Add language switcher
- [ ] Translate all content

#### Job 7.2: Content Creation
- [ ] Create detailed Yoga descriptions
- [ ] Create Dosha descriptions
- [ ] Create planetary effect descriptions
- [ ] Create house significations content
- [ ] Create Rashi characteristics content

#### Job 7.3: SEO & Marketing
- [ ] Add meta tags
- [ ] Create sitemap.xml
- [ ] Add structured data
- [ ] Create robots.txt
- [ ] Set up Google Analytics
- [ ] Set up Search Console

#### Job 7.4: Documentation
- [ ] Create user guide
- [ ] Create API documentation
- [ ] Create admin documentation
- [ ] Create contribution guidelines

#### Job 7.5: Deployment
- [ ] Deploy frontend to Vercel
- [ ] Deploy backend to Railway/Render
- [ ] Set up production database
- [ ] Configure custom domain
- [ ] Set up SSL certificates
- [ ] Configure CDN

#### Job 7.6: Monitoring & Analytics
- [ ] Set up error tracking (Sentry)
- [ ] Set up uptime monitoring
- [ ] Set up performance monitoring
- [ ] Create admin dashboard

**Commit Point:** `feat(phase7): Production release`

---

## Timeline Estimates

| Phase | Duration | Cumulative |
|-------|----------|------------|
| Phase 0 | 2 days | 2 days |
| Phase 1 | 3 days | 5 days |
| Phase 2 | 5 days | 10 days |
| Phase 3 | 7 days | 17 days |
| Phase 4 | 6 days | 23 days |
| Phase 5 | 10 days | 33 days |
| Phase 6 | 4 days | 37 days |
| Phase 7 | 5 days | 42 days |

**Total Estimated Time: ~6 weeks (full-time)**

---

## Key Milestones

1. **Week 1:** Knowledge extraction complete, project setup done
2. **Week 2:** Core calculations working, tests passing
3. **Week 3:** Advanced features (Dasha, Yogas) complete
4. **Week 4:** Backend API complete
5. **Week 5:** Frontend development complete
6. **Week 6:** Integration complete, production deployment

---

## Commit Message Convention

```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Formatting changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples:**
- `feat(astro): Add Vimshottari Dasha calculator`
- `fix(api): Correct ascendant calculation for southern hemisphere`
- `docs(readme): Update setup instructions`
- `test(kundali): Add unit tests for chart generation`

---

## Branching Strategy

```
main (production)
  └── develop (integration)
        └── feature/phase-2-astro-engine
        └── feature/phase-3-dasha
        └── feature/phase-4-backend
        └── feature/phase-5-frontend
        └── hotfix/fix-calculation-bug
```

---

*Last Updated: March 26, 2026*
*Next Milestone: Phase 1 Completion*
