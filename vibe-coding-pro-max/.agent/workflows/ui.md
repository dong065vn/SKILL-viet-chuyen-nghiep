---
description: Làm đẹp giao diện UI/UX với Design Intelligence (50+ styles, 97 palettes, 57 fonts, 9+ stacks)
---

# /ui - UI/UX Pro Max Polish

## Cách dùng
```
/ui [component/page]         # Làm đẹp component cụ thể
/ui audit                    # Audit toàn bộ UI
/ui design [mô tả project]  # Generate design system hoàn chỉnh
```

## ⚠️ NGUYÊN TẮC

> **LUÔN generate design system TRƯỚC khi code UI.**
> Không đoán colors, fonts. Dùng search engine để chọn.

## Quy trình

### Step 1: Analyze Requirements
1. Xác định từ user request:
   - **Product type**: SaaS, e-commerce, portfolio, dashboard, landing page, blog...
   - **Style keywords**: minimal, playful, professional, elegant, dark mode...
   - **Industry**: healthcare, fintech, gaming, education, beauty...
   - **Stack**: React, Vue, Next.js, html-tailwind (default)

### Step 2: Generate Design System (BẮT BUỘC)

**Luôn chạy trước khi làm UI:**

```bash
python3 .antigravity/skills/uiux/ui-ux-pro-max/scripts/search.py "<product_type> <industry> <keywords>" --design-system [-p "Project Name"]
```

Output bao gồm:
- ✅ UI Pattern recommendation
- ✅ Style (glassmorphism, minimalism, etc.)
- ✅ Color palette hoàn chỉnh
- ✅ Font pairing (Google Fonts)
- ✅ Effects & animations
- ✅ Anti-patterns cần tránh

**Ví dụ:**
```bash
# SaaS Dashboard
python3 .antigravity/skills/uiux/ui-ux-pro-max/scripts/search.py "saas dashboard analytics" --design-system -p "DataViz Pro"

# Landing page dịch vụ spa
python3 .antigravity/skills/uiux/ui-ux-pro-max/scripts/search.py "beauty spa wellness service elegant" --design-system -p "Serenity Spa"

# E-commerce store
python3 .antigravity/skills/uiux/ui-ux-pro-max/scripts/search.py "ecommerce fashion modern luxury" --design-system -p "StyleHub"
```

### Step 3: Detailed Searches (bổ sung khi cần)

```bash
# Thêm style options
python3 .antigravity/skills/uiux/ui-ux-pro-max/scripts/search.py "glassmorphism dark" --domain style

# UX best practices
python3 .antigravity/skills/uiux/ui-ux-pro-max/scripts/search.py "animation accessibility" --domain ux

# Font alternatives
python3 .antigravity/skills/uiux/ui-ux-pro-max/scripts/search.py "elegant luxury serif" --domain typography

# Chart recommendations
python3 .antigravity/skills/uiux/ui-ux-pro-max/scripts/search.py "real-time dashboard" --domain chart

# Landing page structure
python3 .antigravity/skills/uiux/ui-ux-pro-max/scripts/search.py "hero social-proof pricing" --domain landing
```

### Step 4: Stack Guidelines

```bash
# Get best practices cho stack đang dùng
python3 .antigravity/skills/uiux/ui-ux-pro-max/scripts/search.py "responsive layout form" --stack html-tailwind
```

**Available stacks:** `html-tailwind`, `react`, `nextjs`, `vue`, `svelte`, `swiftui`, `react-native`, `flutter`, `shadcn`

### Step 5: UI Audit & Polish
4. **Visual improvements:**
   - Modern typography (từ design system)
   - Smooth gradients thay vì flat colors
   - Micro-animations (hover, transition, loading)
   - Glassmorphism, subtle shadows
5. **Interaction design:**
   - Hover effects (color/opacity, KHÔNG scale gây shift)
   - Loading states (skeleton, spinner)
   - Error states (inline messages)
   - Empty states (helpful illustrations)
   - **cursor-pointer** cho mọi element clickable
6. **Accessibility (WCAG 2.1):**
   - Color contrast ≥ 4.5:1
   - Focus indicators rõ ràng
   - Alt text cho images
   - Keyboard navigation
   - `prefers-reduced-motion` respected

### Step 6: Responsive
7. Mobile-first approach
8. Breakpoints: 375px (xs), 640px (sm), 768px (md), 1024px (lg), 1440px (xl)
9. Test trên multiple viewports

## Search Domains

| Domain | Dữ liệu | Ví dụ keywords |
|--------|----------|----------------|
| `product` | Gợi ý theo loại sản phẩm | SaaS, e-commerce, portfolio, healthcare |
| `style` | 50+ UI styles + CSS keywords | glassmorphism, minimalism, brutalism, dark |
| `typography` | 57 font pairings (Google Fonts) | elegant, playful, professional, modern |
| `color` | 97 color palettes | saas, ecommerce, healthcare, beauty, fintech |
| `landing` | Cấu trúc landing page | hero, testimonial, pricing, social-proof |
| `chart` | 25 loại chart + libraries | trend, comparison, funnel, pie, timeline |
| `ux` | 99 UX guidelines | animation, accessibility, z-index, loading |

## ❌ Anti-patterns (TRÁNH)

| Sai | Đúng |
|-----|------|
| Dùng emoji làm icon (🎨 🚀) | Dùng SVG icons (Heroicons, Lucide) |
| Scale transform gây layout shift | Color/opacity transition |
| `bg-white/10` trong light mode | `bg-white/80` hoặc cao hơn |
| Text gray-400 trong light mode | Text slate-600 minimum |
| Mix container widths | Consistent `max-w-6xl` hoặc `max-w-7xl` |
| Navbar dính `top-0` | Floating navbar `top-4 left-4 right-4` |

## ✅ Pre-Delivery Checklist

- [ ] Design system đã generate (search engine)
- [ ] No emojis dùng làm icons
- [ ] Consistent icon set (Heroicons/Lucide)
- [ ] `cursor-pointer` cho mọi clickable elements
- [ ] Transitions smooth (150-300ms)
- [ ] Contrast ≥ 4.5:1 cho text
- [ ] Responsive: 375px, 768px, 1024px, 1440px
- [ ] No horizontal scroll on mobile
- [ ] Light/dark mode tested (nếu có)
- [ ] Alt text cho images, labels cho forms

## Skills sử dụng
- `ui-ux-pro-max` - Design intelligence (search engine + databases)
- `frontend-design` - Frontend aesthetics
- `wcag-audit-patterns` - Accessibility
- `tailwind-design-system` - Design system

## Output
- Design system recommendation (from search engine)
- Updated UI components
- Design tokens/variables
- Responsive layouts
- Accessibility improvements
