import { defineCollection } from 'astro:content';
import { file } from 'astro/loaders';
import { z } from 'astro/zod';

const optionalLink = z.string().optional();

const profile = defineCollection({
  loader: file('content/profile.yaml'),
  schema: z.object({
    name: z.string(),
    role: z.string(),
    affiliation: z.string(),
    location: z.string(),
    email: z.email(),
    introduction: z.string(),
    biography: z.array(z.string()),
    profileImage: z.string(),
    heroImage: z.string(),
    footerImage: z.string(),
    interests: z.array(z.object({
      title: z.string(),
      description: z.string(),
    })),
    links: z.array(z.object({
      label: z.string(),
      url: z.string(),
    })),
    navigation: z.array(z.object({
      label: z.string(),
      href: z.string(),
    })),
  }),
});

const publications = defineCollection({
  loader: file('content/publications.yaml'),
  schema: z.object({
    title: z.string(),
    titleZh: z.string().optional(),
    authors: z.string(),
    venue: z.string(),
    year: z.number().int(),
    selected: z.boolean().default(false),
    doi: optionalLink,
    pdf: optionalLink,
    project: optionalLink,
    website: optionalLink,
  }),
});

const projects = defineCollection({
  loader: file('content/projects.yaml'),
  schema: z.object({
    title: z.string(),
    period: z.string(),
    description: z.string(),
    url: optionalLink,
  }),
});

const experience = defineCollection({
  loader: file('content/experience.yaml'),
  schema: z.object({
    type: z.enum(['education', 'experience']),
    institution: z.string(),
    role: z.string(),
    period: z.string(),
    description: z.string().optional(),
  }),
});

export const collections = { profile, publications, projects, experience };
