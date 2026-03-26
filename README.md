# 🪐 Bastusastra - Vedic Astrology Platform

A comprehensive web application for Vedic astrology (Jyotish) calculations, birth chart (Kundali) generation, Panchang, Muhurta finder, and horoscope matching.

## 📚 Knowledge Base

Built from classical astrology texts:
- **Predictive Astrology of the Hindus** by Pandit Gopesh Kumar Ojha (358 pages)
- **Jataka Parijata** by Vaidyanatha Dikshita (324 pages)
- **Brihat Jataka** by V. Subrahmanya Sastri (588 pages - OCR in progress)

## 🏗️ Architecture

```
bastusastra/
├── frontend/          # Next.js 14 + TypeScript + Tailwind CSS
├── backend/           # Node.js + Express + Prisma ORM
├── astro-engine/      # Pure TypeScript astrology calculation library
├── database/          # Migrations and seeds
└── docker-compose.yml # Local development environment
```

## 🚀 Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | Next.js 14, React 19, TypeScript, Tailwind CSS |
| **Backend** | Node.js, Express, Prisma ORM |
| **Database** | PostgreSQL 15, Redis 7 |
| **Astro Engine** | TypeScript (zero dependencies) |
| **DevOps** | Docker, Docker Compose |

## 🛠️ Quick Start

### Prerequisites
- Node.js 18+
- Docker & Docker Compose
- Git

### 1. Clone Repository

```bash
git clone git@github.com:Raman21676/bastusastra.git
cd bastusastra
```

### 2. Setup Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your configuration
nano .env
```

### 3. Start Database Services

```bash
docker-compose up -d
```

### 4. Setup Backend

```bash
cd backend
npm install
npx prisma migrate dev
npm run dev
```

### 5. Setup Frontend

```bash
cd frontend
npm install
npm run dev
```

### 6. Access Application

- Frontend: http://localhost:3000
- Backend API: http://localhost:3001
- Prisma Studio: http://localhost:5555 (run `npx prisma studio` in backend)

## 📖 Features

### Core Astrology Calculations
- ✅ Ayanamsa (Lahiri) calculation
- ✅ Julian Day Number conversion
- ✅ Sidereal time calculation
- ✅ Planetary position calculations
- ✅ Ascendant (Lagna) calculation
- ✅ House calculations (Equal, Placidus)

### Birth Chart (Kundali)
- ✅ Janma Kundali (D-1) generation
- ✅ 16 Divisional Charts (Vargas):
  - Hora (D-2), Drekkana (D-3), Navamsa (D-9)
  - Dasamamsa (D-10), Dwadasamsa (D-12)
  - Saptamamsa (D-7), Trimsamsa (D-30)
  - And more...

### Dasha Systems
- ✅ Vimshottari Dasha calculation
- ✅ Antardasha (Bhukti) calculation
- ✅ Pratyantardasha calculation

### Panchang
- ✅ Daily Panchang (Tithi, Nakshatra, Yoga, Karana)
- ✅ Sunrise/Sunset calculation
- ✅ Rahu Kaal, Yamaganda, Gulika
- ✅ Choghadiya Muhurta

### Compatibility
- ✅ Ashta Koota (8-fold matching system)
  - Varna, Vashya, Tara, Yoni
  - Graha Maitri, Gana, Bhakoot, Nadi
- ✅ Mangal Dosha (Manglik) detection

### Yoga & Dosha Detection
- ✅ Raj Yoga detection
- ✅ Dhana Yoga detection
- ✅ Gaja Kesari Yoga
- ✅ Mangal Dosha detection
- ✅ Kaal Sarp Dosha detection

### Horoscope
- Daily, Weekly, Monthly, Yearly horoscopes
- Transit analysis
- Rashi-based predictions

## 📝 Project Structure

```
bastusastra/
├── frontend/              # Next.js Application
│   ├── src/app/          # App Router pages
│   ├── src/components/   # React components
│   └── public/           # Static assets
├── backend/              # Express API
│   ├── src/controllers/  # Route controllers
│   ├── src/services/     # Business logic
│   ├── src/routes/       # API routes
│   └── prisma/           # Database schema
├── astro-engine/         # Astrology calculations
│   ├── src/core/         # Core calculations
│   ├── src/charts/       # Chart generation
│   ├── src/dasha/        # Dasha systems
│   ├── src/analysis/     # Yoga/Dosha detection
│   ├── src/matching/     # Compatibility
│   └── src/muhurta/      # Auspicious times
└── docs/                 # Documentation
    ├── knowledge-base.md # Extracted book knowledge
    ├── algorithms.md     # Calculation pseudo-code
    └── PROJECT_PLAN.md   # Development roadmap
```

## 🧪 Testing

```bash
# Backend tests
cd backend
npm test

# Astro engine tests
cd astro-engine
npm test

# Frontend tests
cd frontend
npm test
```

## 📚 Documentation

- [Project Plan](docs/PROJECT_PLAN.md) - Complete development roadmap
- [Knowledge Base](docs/knowledge-base.md) - Extracted formulas and rules
- [Algorithms](docs/algorithms.md) - Calculation pseudo-code
- [API Documentation](docs/api/) - API endpoints (coming soon)

## 🗺️ Roadmap

- [x] Phase 0: Knowledge extraction from books
- [x] Phase 1: Project setup and infrastructure
- [ ] Phase 2: Core astro engine implementation
- [ ] Phase 3: Backend API development
- [ ] Phase 4: Frontend UI development
- [ ] Phase 5: Testing and deployment

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Pandit Gopesh Kumar Ojha for "Predictive Astrology of the Hindus"
- Vaidyanatha Dikshita for "Jataka Parijata"
- V. Subrahmanya Sastri for "Brihat Jataka"

---

Built with ❤️ for preserving and sharing Vedic astrology knowledge.
