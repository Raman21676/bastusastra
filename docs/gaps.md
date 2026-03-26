# Bastusastra - Knowledge Gaps & TODOs

This document identifies gaps in the extracted knowledge from the three astrology books and tracks items that need additional research or implementation.

---

## Critical Gaps

### 1. Brihat Jataka Content
**Status:** ⚠️ HIGH PRIORITY

The Brihat Jataka (2nd Edition) by V. Subrahmanya Sastri is a scanned PDF without OCR text layer. This is one of the most important classical texts on Hindu astrology.

**Action Items:**
- [ ] Extract text using OCR (Optical Character Recognition)
- [ ] Alternative: Use existing English translations if available
- [ ] Key areas to extract:
  - Detailed planetary combinations (Yogas)
  - Advanced Dasha interpretation rules
  - Specific timing techniques
  - Raja Yoga definitions
  - Maraka (death-inflicting) planet rules

**Estimated Impact:** HIGH - This book contains many advanced techniques not covered in the other two books.

---

### 2. Ephemeris Calculation Algorithms
**Status:** ⚠️ HIGH PRIORITY

The books provide formulas but not complete algorithms for planetary positions.

**Missing Components:**
- [ ] VSOP87 (Variations Séculaires des Orbites Planétaires) implementation for precise planetary positions
- [ ] ELP-2000 (Ephemeride Lunaire Parisienne) for accurate Moon positions
- [ ] Precession and nutation calculations beyond basic Lahiri ayanamsa
- [ ] Planetary latitude calculations (though noted as less important in Hindu astrology)
- [ ] Retrogression detection algorithms
- [ ] Stationary point calculations

**Recommended Solution:**
Use Swiss Ephemeris library (`swisseph` or `ephem` in Python, or `swisseph` npm package for Node.js) for accurate calculations.

---

### 3. House Division Systems
**Status:** ⚠️ MEDIUM PRIORITY

The books mention house calculations but don't provide complete algorithms for all systems.

**Missing Systems:**
- [ ] Placidus house system (most commonly used)
- [ ] Koch house system
- [ ] Campanus house system
- [ ] Porphyry house system
- [ ] Regiomontanus house system
- [ ] Whole Sign system (traditional)
- [ ] Sripati method (specific to Indian astrology)

**Current Implementation:**
- Equal house system (implemented in algorithms.md)
- Basic Placidus outline (needs completion)

---

### 4. Advanced Dasha Systems
**Status:** ⚠️ MEDIUM PRIORITY

Only Vimshottari Dasha is fully covered. Other important dasha systems need documentation:

**Missing Dasha Systems:**
- [ ] Yogini Dasha (36 years cycle)
- [ ] Ashtottari Dasha (108 years cycle)
- [ ] Kalachakra Dasha
- [ ] Chara Dasha (Jaimini system)
- [ ] Narayana Dasha
- [ ] Drigdasha
- [ ] Sudarshana Chakra Dasha

---

### 5. Muhurta (Electional Astrology) Details
**Status:** ⚠️ MEDIUM PRIORITY

Basic Panchang elements are covered, but detailed Muhurta rules are sparse:

**Missing Muhurta Calculations:**
- [ ] Choghadiya Muhurta detailed calculation
- [ ] Hora Chakra for each day
- [ ] Abhijit Muhurta calculation
- [ ] Marriage Muhurta specific rules
- [ ] Griha Pravesh (house warming) Muhurta
- [ ] Naamkaran (naming ceremony) Muhurta
- [ ] Annaprashan (first feeding) Muhurta
- [ ] Upanayana (sacred thread) Muhurta
- [ ] Vehicle purchase Muhurta
- [ ] Business start Muhurta

**Partial Information Available:**
- Rahu Kaal calculation (implemented)
- Yamaganda calculation (implemented)
- Gulika calculation (needs refinement)

---

### 6. Gochara (Transit) Analysis
**Status:** ⚠️ MEDIUM PRIORITY

Basic transit rules mentioned but not comprehensive:

**Missing Transit Rules:**
- [ ] Detailed Saturn transit effects (Ashtama Shani, etc.)
- [ ] Jupiter transit effects for each house
- [ ] Sade Sati detailed analysis (3 phases)
- [ ] Kantaka Shani rules
- [ ] Double transit of Jupiter and Saturn
- [ ] Transit from Moon vs. Ascendant vs. Arudha Lagna
- [ ] Varshaphala (annual horoscope) techniques

---

### 7. Divisional Chart (Varga) Interpretations
**Status:** ⚠️ LOW-MEDIUM PRIORITY

Calculations are documented, but interpretation rules are limited:

**Missing Varga Interpretations:**
- [ ] Detailed Navamsa (D-9) interpretation rules
- [ ] Dasamamsa (D-10) career analysis
- [ ] Saptamamsa (D-7) children analysis
- [ ] Dwadasamsa (D-12) parent analysis
- [ ] Shodasamsa (D-16) vehicle analysis
- [ ] Vimsamsa (D-20) spiritual analysis
- [ ] Chaturvimsamsa (D-24) education analysis

---

### 8. Ashtakavarga System
**Status:** ⚠️ MEDIUM PRIORITY

Not covered in the extracted books, but essential for detailed prediction:

**Missing Ashtakavarga Components:**
- [ ] Sarva Ashtakavarga calculation
- [ ] Prastara Ashtakavarga
- [ ] Samudaya Ashtakavarga
- [ ] Kakshya (division) rules
- [ ] Bindu and Rekha interpretations
- [ ] Ashtakavarga transits
- [ ] Sodhya Pinda calculations

---

### 9. Shadbala (Six-Fold Strength)
**Status:** ⚠️ LOW PRIORITY

Planetary strength calculations mentioned but not detailed:

**Missing Shadbala Components:**
- [ ] Sthana Bala (positional strength)
- [ ] Dig Bala (directional strength)
- [ ] Kala Bala (temporal strength)
- [ ] Cheshta Bala (motional strength)
- [ ] Naisargika Bala (natural strength)
- [ ] Drik Bala (aspect strength)
- [ ] Ishta and Kashta Phala calculations

---

### 10. Prashna (Horary) Astrology
**Status:** ⚠️ LOW PRIORITY

Not covered in the books, but useful for specific questions:

**Missing Prashna Techniques:**
- [ ] Tarot-like number selection methods
- [ ] Prashna Lagna determination
- [ ] Time-based Prashna charts
- [ ] Lost object recovery techniques
- [ ] Missing person location methods

---

## Technical Implementation Gaps

### 1. Precise Planetary Position Engine
**Current State:** Simplified formulas
**Needed:** Swiss Ephemeris integration

```
Recommended Libraries:
- Python: pyswisseph, skyfield, astropy
- Node.js: swisseph
- Go: go-ephem
```

### 2. Geocoding Service
**Needed for:** Location to coordinates conversion

```
Options:
- Google Maps Geocoding API
- OpenStreetMap Nominatim (free)
- Mapbox Geocoding API
```

### 3. Timezone Database
**Needed for:** Accurate local time calculations

```
Options:
- IANA Time Zone Database (tzdb)
- moment-timezone (JavaScript)
- pytz (Python)
```

### 4. Atlas Database
**Needed for:** City coordinates and timezone lookups

```
Data Sources:
- GeoNames database (free)
- OpenStreetMap data
- Paid: Astro.com atlas, ACS Atlas
```

---

## Content Gaps for Website Features

### 1. Daily/Weekly/Monthly Horoscope
**Missing:** Transit-based prediction rules
- [ ] General transit effects for each Rashi
- [ ] Moon sign based predictions
- [ ] Nakshatra-based daily guidance

### 2. Detailed Yoga Interpretations
**Missing:** Effects of hundreds of yogas
- [ ] Effects of Raja Yogas
- [ ] Effects of Dhana Yogas
- [ ] Effects of Arista Yogas (negative combinations)
- [ ] Effects of Neecha Bhanga Raja Yoga

### 3. Remedial Measures
**Missing:** Upaya (remedial) recommendations
- [ ] Gemstone recommendations
- [ ] Mantra recommendations
- [ ] Puja recommendations
- [ ] Donation/charity recommendations
- [ ] Fasting recommendations

### 4. Medical Astrology
**Missing:** Body part and disease correlations
- [ ] House-body part mapping
- [ ] Planet-disease correlations
- [ ] Timing of health issues

---

## Priority Matrix

| Gap | Priority | Complexity | Impact |
|-----|----------|------------|--------|
| Brihat Jataka OCR | HIGH | MEDIUM | HIGH |
| Swiss Ephemeris Integration | HIGH | MEDIUM | HIGH |
| House Division Systems | MEDIUM | HIGH | MEDIUM |
| Advanced Dasha Systems | MEDIUM | MEDIUM | MEDIUM |
| Muhurta Details | MEDIUM | MEDIUM | HIGH |
| Transit Analysis | MEDIUM | LOW | HIGH |
| Ashtakavarga | MEDIUM | HIGH | MEDIUM |
| Varga Interpretations | LOW | LOW | MEDIUM |
| Shadbala | LOW | HIGH | LOW |
| Prashna | LOW | HIGH | LOW |

---

## Research Sources to Consult

### Classical Texts (Sanskrit)
1. Brihat Parashara Hora Shastra
2. Phaladeepika
3. Saravali
4. Jataka Parijata (Volume 2)
5. Uttar Kalamrita
6. Daivajna Vallabha

### Modern Reference Books
1. "Planets in Signs and Houses" by B.V. Raman
2. "How to Judge a Horoscope" by B.V. Raman
3. "Astrology of the Seers" by David Frawley
4. "Light on Life" by Hart deFouw
5. "The Art and Science of Vedic Astrology" by Richard Fish

### Online Resources
1. Astro.com (Swiss Ephemeris)
2. Cosmic Insights (mobile app reference)
3. AstroSage (algorithm references)

---

## Implementation Plan

### Phase 0 Completion (Knowledge Extraction)
- [x] Extract Book 1: Predictive Astrology of the Hindus
- [x] Extract Book 2: Jataka Parijata Vol 1
- [ ] OCR Book 3: Brihat Jataka (pending)
- [x] Create knowledge-base.md
- [x] Create algorithms.md
- [x] Document gaps

### Next Steps for Gap Filling
1. **Immediate (Week 1):**
   - Set up Swiss Ephemeris integration
   - Implement basic Placidus house system
   - Test planetary position accuracy

2. **Short Term (Weeks 2-3):**
   - Complete Vimshottari Dasha with all levels
   - Implement complete Ashta Koota matching
   - Add detailed Panchang with all elements

3. **Medium Term (Weeks 4-6):**
   - Add Yogini Dasha
   - Implement Ashtakavarga
   - Add detailed Muhurta calculations

4. **Long Term (Ongoing):**
   - Extract Brihat Jataka content
   - Add advanced transit analysis
   - Implement medical astrology correlations

---

*Last Updated: March 26, 2026*
*Next Review: After Brihat Jataka extraction*
