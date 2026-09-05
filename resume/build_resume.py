# -*- coding: utf-8 -*-
"""Builds Sam_Mahdavian_Resume.docx (v9, 2026-09-05) with python-docx.

Source of truth for the text is this file. Export to PDF with Word:
  powershell -File resume/export_pdf.ps1
"""
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

OUT = os.path.join(os.path.dirname(__file__), 'Sam_Mahdavian_Resume.docx')
FONT = 'Calibri'
INK = RGBColor(0x19, 0x18, 0x14)
MUTED = RGBColor(0x5F, 0x5A, 0x4F)
GOLD = RGBColor(0x8A, 0x6A, 0x20)

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Inches(8.5), Inches(11)
sec.left_margin = sec.right_margin = Inches(0.5)
sec.top_margin = Inches(0.4)
sec.bottom_margin = Inches(0.4)

st = doc.styles['Normal']
st.font.name = FONT
st.font.size = Pt(9.5)
st.element.rPr.rFonts.set(qn('w:eastAsia'), FONT)
st.paragraph_format.space_after = Pt(0)
st.paragraph_format.space_before = Pt(0)
st.paragraph_format.line_spacing = 1.0

def para(text='', size=None, bold=False, italic=False, color=None, align=None, after=0, before=0, keep=False):
    p = doc.add_paragraph()
    if align: p.alignment = align
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.space_before = Pt(before)
    if keep: p.paragraph_format.keep_with_next = True
    if text:
        r = p.add_run(text)
        r.bold = bold; r.italic = italic
        if size: r.font.size = Pt(size)
        if color: r.font.color.rgb = color
    return p

def run(p, text, bold=False, italic=False, size=None, color=None):
    r = p.add_run(text); r.bold = bold; r.italic = italic
    if size: r.font.size = Pt(size)
    if color: r.font.color.rgb = color
    return r

def hyperlink(p, text, url, size=9, color=RGBColor(0x15, 0x5F, 0x58)):
    part = p.part
    r_id = part.relate_to(url, 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink', is_external=True)
    h = OxmlElement('w:hyperlink'); h.set(qn('r:id'), r_id)
    r = OxmlElement('w:r'); rPr = OxmlElement('w:rPr')
    rf = OxmlElement('w:rFonts'); rf.set(qn('w:ascii'), FONT); rf.set(qn('w:hAnsi'), FONT); rPr.append(rf)
    c = OxmlElement('w:color'); c.set(qn('w:val'), '%02X%02X%02X' % (color[0], color[1], color[2])); rPr.append(c)
    sz = OxmlElement('w:sz'); sz.set(qn('w:val'), str(int(size * 2))); rPr.append(sz)
    u = OxmlElement('w:u'); u.set(qn('w:val'), 'single'); rPr.append(u)
    r.append(rPr); t = OxmlElement('w:t'); t.text = text; t.set(qn('xml:space'), 'preserve'); r.append(t)
    h.append(r); p._p.append(h)

def heading(text):
    p = para(text, size=10, bold=True, color=GOLD, before=7, after=2, keep=True)
    pPr = p._p.get_or_add_pPr()
    bdr = OxmlElement('w:pBdr'); b = OxmlElement('w:bottom')
    b.set(qn('w:val'), 'single'); b.set(qn('w:sz'), '6'); b.set(qn('w:space'), '1'); b.set(qn('w:color'), 'C9BFA6')
    bdr.append(b); pPr.append(bdr)
    return p

def bullet(text, lead=None):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.left_indent = Inches(0.18)
    p.paragraph_format.first_line_indent = Inches(-0.14)
    p.paragraph_format.space_after = Pt(1.5)
    if lead:
        run(p, lead, bold=True)
    run(p, text)
    return p

def job(company, role, place, dates):
    p = para(before=4, after=1, keep=True)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(7.5), WD_TAB_ALIGNMENT.RIGHT)
    run(p, company + '  ', bold=True, size=10.5)
    run(p, role, bold=True, size=10, color=MUTED)
    run(p, '\t' + place + '   ·   ' + dates, size=9, color=MUTED)

def comp(lead, text):
    p = para(after=1.5)
    run(p, lead + ':  ', bold=True)
    run(p, text)

# ---------------- Header ----------------
para('SAM MAHDAVIAN, PhD, PMP, PMI-PBA', size=17, bold=True, color=INK, after=0)
para('AI Solutions & Delivery Lead  ·  Founder & CEO, Brane', size=11, bold=True, color=MUTED, after=1)
para('Agentic systems that solve the business problem. Tested, governed, and safe in regulated production.', size=9.5, italic=True, color=MUTED, after=2)
p = para(after=1)
run(p, 'Orlando, FL   ·   407-808-3580   ·   ', size=9, color=MUTED)
hyperlink(p, 'sam@sammahdavian.ai', 'mailto:sam@sammahdavian.ai')
run(p, '   ·   ', size=9, color=MUTED)
hyperlink(p, 'sammahdavian.ai', 'https://sammahdavian.ai/')
run(p, '   ·   ', size=9, color=MUTED)
hyperlink(p, 'LinkedIn', 'https://www.linkedin.com/in/mahdavian-sam/')
run(p, '   ·   ', size=9, color=MUTED)
hyperlink(p, 'GitHub', 'https://github.com/amiiiirsaman')
run(p, '   ·   ', size=9, color=MUTED)
hyperlink(p, 'Google Scholar', 'https://scholar.google.com/citations?user=DI4-4N0AAAAJ')
run(p, '   ·   ', size=9, color=MUTED)
hyperlink(p, 'AWS Blog', 'https://aws.amazon.com/blogs/architecture/automating-contract-intelligence-with-doczy-ai-on-aws/')

# ---------------- Summary ----------------
heading('PROFESSIONAL SUMMARY')
para('AI solutions leader who turns ambiguous business problems into agentic systems that hold up in regulated production. '
     'I work as a single-threaded owner from discovery and pre-sales through reference architecture, build, and adoption, and every system I ship has to clear one test: '
     'it solves the business problem, it is evaluated against real cases, and it is safe to run. Across healthcare, financial services, transportation, retail, and manufacturing '
     'I have shipped 40+ systems and 150+ agents that together produced $40M+ in revenue and $500M+ in identified client savings, and I have authored 50+ Claude skills that specialize '
     'those agents into repeatable, gated engines. I also co-founded and run Brane, an AI siting-and-planning startup, as CEO. For 15+ years I have been the translator between the '
     'C-suite that wants ROI and the engineers who build, pairing LLM/RAG and AWS engineering with executive-facing delivery. PhD (ML / applied AI); PMP; PMI-PBA.', after=1)

# ---------------- Competencies ----------------
heading('CORE COMPETENCIES')
comp('Solutions & Pre-Sales', 'enterprise AI delivery, solution architecture, discovery to design to deploy to adopt, requirements elicitation across sectors, pre-sales and POCs, buyer-persona and commercial market analysis, ROI and business-case framing, single-threaded ownership, executive enablement.')
comp('Agentic AI & GenAI', 'LangChain/LangGraph, Strands SDK, CrewAI, Claude Code and custom Python; multi-agent orchestration; agent specialization through 50+ authored skills (workflow, capability, domain) with approval gates and append-only decision logs as agent memory; MCP tool design; RAG and vector DBs; guardrails, evals, and human-in-the-loop; prompt engineering; latency/cost/accuracy optimization; AWS Bedrock and AgentCore; Claude and OpenAI.')
comp('Production & MLOps', 'AWS (Bedrock, SageMaker, Lambda, Step Functions, S3, ECS/EKS), Docker, Kubernetes, CI/CD, IaC (Terraform/CDK), model serving and LLMOps, observability, model-risk governance, IAM and cloud security, HITRUST/HIPAA, FinOps.')
comp('Leadership & Delivery', 'team building and mentorship (orgs to ~25), roadmap and solution ownership, GTM, pricing and packaging, Agile/Scrum and SAFe, storytelling with data, hiring and talent development.')

# ---------------- Experience ----------------
heading('PROFESSIONAL EXPERIENCE')
job('AArete LLC', 'Director, Data Science & AI', 'Orlando, FL', '2022 - Present')
bullet('Designed the architecture and led the build of Doczy.ai, a multi-tenant GenAI platform on AWS (retrieval, prompt orchestration, agentic tool-calling, dynamic model selection, governance, observability). Scaled it to 2.5M+ contracts and 442B+ tokens at 99%+ accuracy under HITRUST/HIPAA, generating $15M+ in revenue and $330M+ in client savings. Architecture featured on the AWS Architecture Blog; issued a U.S. patent in 2025.')
bullet('Built 40+ systems and 150+ agents that each solve a specific business problem, most now in production, on LangChain/LangGraph, Strands SDK, Claude Code, and custom Python over AWS Bedrock and AgentCore. Across the portfolio these systems produced $40M+ in revenue and $500M+ in identified client savings. Every one is evaluated against real cases before release, tuned for latency, cost, and accuracy, and built human-in-the-loop and audit-first.')
bullet('Authored 50+ Claude skills across 12 engine repositories that turn one-off agent work into repeatable, gated procedures: workflow skills (investigate, requirements with an approval gate, build, test), capability skills (PHI/PII pre-flight, engine repeatability, cost observability), and domain skills per engine. Result: any teammate regenerates a deliverable from a clean clone with one command, and a strict split between LLM judgment and deterministic precision is enforced by the tooling, not by discipline.')
bullet('Built an AI claims-testing automation engine for a Medicaid managed-care plan that derives what each claim should pay from contract text and the state’s published rate files, with no LLM anywhere in the pricing chain: 394 traceable test cases from 102 contract rules, backtested against 213,420 historical claim lines, 460+ automated tests, regenerated in minutes from one command, roughly 100× faster than hand-written test authoring. Progressed the work from business development to a signed SOW.')
bullet('Run discovery and pre-sales as a single-threaded owner across 10+ Fortune 500 engagements. I sit with executives and business teams, map the real pain by sector, and convert ambiguous problems into structured SOWs and roadmaps. Recently won a $700K+ engagement with an equipment-finance lender, plus $2.5M+ in competitive government and industry RFPs.')
bullet('Own production deployment (Docker, ECS/EKS, CI/CD, IaC, Bedrock/SageMaker serving) and authored the firm’s AI-governance framework: model-risk management, bias and drift monitoring, explainability, prompt-injection defense, confidence-scored human-in-the-loop, and a four-stage maturity model that gates every system before it ships.')
bullet('Lead and mentor ~15 AI scientists and engineers across backend, frontend, and DevOps, plus a business-translation layer that turns stakeholder needs into specs and prompts. Run the firm-wide AI delivery program: ~$1.3M budget, 10+ concurrent workstreams, a six-gate value framework, and value-based pricing that protects margin as delivery cost falls.')
bullet('Lead executive AI-enablement workshops; one for 40+ leaders at an S&P 500 global manufacturer produced a 30% productivity increase and 20+ prioritized use cases. Earlier (Manager / Sr. Data Scientist), built an AI/ML Accelerator that cut modeling cycles ~75% and an ML suite proving a 4.1% registration uplift worth $9.6M in new annual revenue.')

job('Brane (SPLUSM LLC)', 'Co-Founder & CEO', 'Orlando, FL', '2020 - Present')
bullet('Co-founded and lead Brane Mobility, a cloud-native B2B SaaS that turns raw mobility and urban data into multi-scenario, stakeholder-ready insights in minutes for city planners, public agencies, and enterprises. Built and led a ~25-person cross-functional org (GenAI and data scientists, data engineers, full-stack developers, UX/UI) and awarded $625K in grants.')
bullet('In 2026 launched Brane AI on the same platform: a data-center siting and approval-intelligence product that screens every census block group in a three-county corridor against 40 indicators (six gating), prices nine mitigation levers with benefit-cost and lifecycle math, and serves developers and county, utility, and water-district reviewers from one scoring object. Every on-screen number reproduces through the product’s own API, enforced by a six-layer test gate; nine roadmap phases shipped.')
bullet('Architected the platform as two integrated systems: a data-management layer (a four-level dataset-to-KPI hierarchy with automated ETL, validation, a custom KPI formula builder, and user-data integration) and a five-step analysis workflow (project definition across 18 problem types, hotspot identification, multi-objective optimization, sensitivity analysis, and automated Word, PDF, and slide reporting). The AI Decision Engine pairs neural-network forecasting and genetic-algorithm optimization with an AWS Bedrock copilot; multi-city pilots showed ~18% operational efficiency gains.')

job('UCF College of Engineering & Computer Science', 'Lead Data Scientist & Researcher', 'Orlando, FL', '2017 - 2020')
bullet('Delivered two production applications with end-to-end data pipelines used by the U.S. Department of Transportation for traffic and cost forecasting; secured competitive USDOT and NSF funding. Led applied-AI research in forecasting, optimization, and simulation, producing 20+ peer-reviewed publications.')

job('Stratus International Contracting Co.', 'Senior Data Analyst', '', '2011 - 2017')
bullet('Built a PMO optimization framework (hybrid genetic algorithm plus constraint-based simulation) and stood up the firm’s first PMI-aligned PMO, cutting 21% of cost and 32% of time across major projects in three years.')

# ---------------- Selected solutions ----------------
heading('SELECTED PRODUCTION AI SOLUTIONS  (BUSINESS OUTCOME FIRST)')
bullet('Cut payer-policy and claims analysis time 90% with a 10% accuracy gain for a top-5 health payer, surfacing millions in recoverable overpayments. A 9-agent LangGraph pipeline generates 200+ Snowflake-ready SQL queries per policy; reused across payers.')
bullet('Cut invoice processing time 92% with a 5% accuracy gain across an airline, a manufacturer, and a large health system with a straight-through invoice agent on AWS Bedrock (Textract plus validation), routing only exceptions to a human.')
bullet('Surfaced spend savings across 14,765 suppliers and 47,489 parts for a Fortune 500 airline: a 10-agent hand-orchestrated pipeline plus a React command center delivered a 98% task-time reduction and a 20% accuracy gain.')
bullet('SpendSphere: a browser-native spend-intelligence platform (React + DuckDB-WASM, zero external requests) over AP spend, 240K MRO parts lines, and payer vendor cost, with an agentic analyst that writes and runs real SQL and cites its figures; every insight is SQL-computed, never LLM-generated, and release is gated by 160+ browser checks driven by six skills.')
bullet('Skills-driven deck builder: eight authored skills take source files to a client-ready PowerPoint on the corporate template; deterministic ground truth traces every dollar, and a QC gate stops the build if an unhedged figure misses its metric by more than 2%. 80% less deck time, zero untraced numbers.')
bullet('Cut unit-cost claims analysis time 35% with a 4% accuracy gain for a state Medicaid program using a 7-agent LangGraph cognitive loop, taking a five-day analysis down to hours.')
bullet('Protected margin on thousands of daily financing deals for an equipment-finance lender. An 8-agent pricing engine (XGBoost risk scoring, reinforcement-learning optimization, SHAP explainability) is targeting a 15 to 20% margin improvement and 60% faster decisions, explainable for compliance, for a newly won $700K+ engagement.')
bullet('Made underwriting transparent and regulator-ready with an 11-agent LangGraph system that scores 11 risk dimensions under a Chief Underwriter orchestrator (XGBoost + SHAP, every decision explained). Open source.')
bullet('Built contract review that ships itself: a 7-agent clause-assessment engine rates every clause P/A/D/U from a tool-called rubric (criteria never hard-coded), with deterministic guards, an independent QC agent, and human routing for anything uncertain; 85% of assessments validated to auto-approve.')
bullet('Caught the fraud rings rules miss with a 3-agent LangGraph investigation (graph neural net plus LLM) over a 3D transaction graph. Open source.')

# ---------------- Education ----------------
heading('EDUCATION & CERTIFICATIONS')
p = para(after=1.5)
run(p, 'Ph.D., Engineering, University of Central Florida.  ', bold=True)
run(p, 'Dissertation: machine-learning algorithms for forecasting (ML / applied-AI methods).  ')
run(p, 'M.S., Engineering, UCF.  ', bold=True)
run(p, 'Executive Education, Business Administration, Harvard Business School.', bold=True)
comp('Certifications', 'PMP · PMI-PBA · Certified SAFe Practitioner · Advanced Data Science Fellowship (The Data Incubator) · Claude Certified Architect, Anthropic (expected 2026) · AWS Solutions Architect Associate (expected 2026).')

# ---------------- Publications ----------------
heading('PUBLICATIONS, PATENTS & RECOGNITION')
comp('Patent & features', 'U.S. Patent (2025), GenAI contract-intelligence method (Doczy.ai) · featured on the AWS Architecture Blog · founder of Modern AI Academy, teaching how agentic AI is built and shipped.')
comp('Research', '20+ peer-reviewed publications, 460 citations, h-index 10, i10-index 10 (Google Scholar, Sept 2026), in IEEE Access, MDPI, and the ASCE Journal of Construction Engineering & Management. Most-cited: drivers and barriers to connected, automated, shared, and electric vehicles (IEEE Access, 139 citations). Reviewer for the Journal of Intelligent Transportation Systems and TRB.')

doc.core_properties.title = 'Sam Mahdavian Resume'
doc.core_properties.author = 'Sam Mahdavian'
doc.save(OUT)
print('wrote', OUT)
