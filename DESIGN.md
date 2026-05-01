---
name: Civitas Paraíso
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#41474f'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#717880'
  outline-variant: '#c1c7d0'
  surface-tint: '#166396'
  primary: '#004269'
  on-primary: '#ffffff'
  primary-container: '#005a8d'
  on-primary-container: '#a0d0ff'
  inverse-primary: '#96ccff'
  secondary: '#7c5800'
  on-secondary: '#ffffff'
  secondary-container: '#ffbe3c'
  on-secondary-container: '#704e00'
  tertiary: '#5d3500'
  on-tertiary: '#ffffff'
  tertiary-container: '#7e4900'
  on-tertiary-container: '#ffbe7c'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#cee5ff'
  primary-fixed-dim: '#96ccff'
  on-primary-fixed: '#001d32'
  on-primary-fixed-variant: '#004a76'
  secondary-fixed: '#ffdea8'
  secondary-fixed-dim: '#fbbc3a'
  on-secondary-fixed: '#271900'
  on-secondary-fixed-variant: '#5e4200'
  tertiary-fixed: '#ffdcbd'
  tertiary-fixed-dim: '#ffb86e'
  on-tertiary-fixed: '#2c1600'
  on-tertiary-fixed-variant: '#693c00'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  h1:
    fontFamily: Public Sans
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Public Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-md:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  caption:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: '0'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
  section-padding: 80px
---

## Brand & Style

This design system establishes a bridge between institutional reliability and community warmth. It is designed to evoke trust, civic pride, and organized growth for the residents of Barrio El Paraíso. The aesthetic leans into a **Corporate / Modern** style, characterized by structured layouts that ensure information accessibility while utilizing vibrant accents to maintain an approachable, neighborhood-centric feel.

The brand personality is authoritative yet helpful—acting as a digital town square where the formal nature of the UNAD institutional identity meets the daily social fabric of Curumaní. The interface prioritizes clarity and ease of use to accommodate a diverse demographic, from students to elderly residents.

## Colors

The palette is rooted in the institutional identity of UNAD, utilizing deep blues to represent stability and education. 

- **Primary Blue (#005A8D):** Used for navigation, primary actions, and headers to anchor the brand.
- **Secondary Gold (#F4B533):** Employed for highlights, secondary call-to-actions, and progress indicators.
- **Accent Orange (#F39200):** Reserved for high-priority alerts, interactive states, and as a terminal point for gradients.
- **Backgrounds:** A clean White (#FFFFFF) is the primary surface color, with Light Gray (#F5F5F5) used to distinguish content sections and create a subtle "layered" effect.
- **Text:** Dark Gray (#333333) ensures high legibility and meets accessibility standards for all body copy and labels.

## Typography

This design system utilizes **Public Sans**, an open-source typeface designed for government and institutional use. It provides a neutral yet friendly tone that conveys transparency.

Headlines are set with tighter letter-spacing and heavier weights to command attention and create a clear hierarchy. Body text prioritizes readability with a generous 1.6x line height. Labels and interactive elements use a semi-bold weight to distinguish them from static content.

## Layout & Spacing

The layout follows a **Fixed Grid** model on desktop (12 columns) and a fluid 4-column model on mobile. 

A strict 8px spatial rhythm is applied to all components to ensure visual harmony. Generous whitespace is a core requirement; sections should be separated by large padding (80px+) to prevent information fatigue. Cards and containers should utilize internal padding of 24px or 32px to maintain a premium, airy feel.

## Elevation & Depth

To maintain a clean and professional appearance, this design system uses **Ambient Shadows** and tonal layering rather than harsh borders.

1.  **Level 0 (Flat):** Used for the main background (White) and structural sidebars.
2.  **Level 1 (Low Elevation):** Soft shadows (0px 4px 20px rgba(0,0,0,0.05)) for content cards and input fields.
3.  **Level 2 (Active/Hover):** Slightly deeper shadows (0px 8px 30px rgba(0,0,0,0.08)) to indicate interactivity.
4.  **Overlay:** High-blur shadows for modals and dropdown menus to separate them from the community feed.

## Shapes

The shape language is defined by a **Rounded** aesthetic (8px - 12px corners). This softens the institutional Blue and Gold palette, making the interface feel more like a community-led initiative and less like a rigid government portal.

- **Standard Buttons/Inputs:** 8px radius.
- **Content Cards:** 12px radius.
- **Badges/Chips:** 100px (Pill-shaped) for high visibility and a modern touch.

## Components

### Buttons
- **Primary Action:** Features a linear gradient from UNAD Blue (#005A8D) to UNAD Orange (#F39200) at a 135-degree angle. Text is white, semi-bold, with a subtle drop shadow to ensure legibility against the gradient.
- **Secondary Action:** Ghost style with a Primary Blue border and text.

### Cards
- White surfaces with 12px rounded corners and Level 1 soft shadows. 
- Headers within cards should use `label-md` for categories and `h3` for titles.

### "Comunidad UNAD" Badge
- **Style:** A pill-shaped badge with a light blue background (10% opacity of #005A8D) and a solid Primary Blue border.
- **Content:** "Comunidad UNAD - Servicio Social" in `label-md` typography.
- **Icon:** A small, minimalist graduation or "handshake" icon placed to the left of the text.

### Input Fields
- Light gray (#F5F5F5) fill with an 8px radius. 
- Focus state: A 2px solid border in Primary Blue with a soft blue outer glow.

### Iconography
- Line-based, minimalist icons with a 2px stroke weight. Icons should be monochrome (Primary Blue) unless they represent specific status changes.