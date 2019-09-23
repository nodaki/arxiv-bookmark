<template>
  <v-row>
    <v-col v-for="(paper, i) in papers" :key="i" sm="12">
      <v-card>
        <v-card-title>{{ paper.entry.title }}</v-card-title>
        <v-card-text>
          <v-clamp autoresize max-lines="3">
            {{ paper.entry.summary }}
          </v-clamp>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import VClamp from 'vue-clamp'
export default {
  components: {
    VClamp
  },
  data () {
    return {
      papers: [
        {
          title: '',
          id: '',
          published: '',
          updated: '',
          summary: '',
          authors: [],
          link: '',
          categories: [],
          comment: ''
        }
      ]
    }
  },
  created () {
    const url = 'https://export.arxiv.org/api/query?search_query=cat:cs.CV&sortBy=lastUpdatedDate&sortOrder=descending'
    this.papers = this.getPapers(url)
  },
  methods: {
    getPapers (url) {
      const Parser = require('rss-parser')
      const options = {
        customFields: {
          item: [
            ['published', 'published'],
            ['updated', 'updated'],
            ['summary', 'summary'],
            ['author', 'authors', { keepArray: true }],
            ['category', 'categories', { keepArray: true }],
            ['arxiv:comment', 'comment']
          ]
        }
      }
      const parser = new Parser(options)
      const papers = []
      parser.parseURL(url).then(function (feed) {
        feed.items.forEach(function (entry) {
          papers.push({ entry })
        })
      })
      return papers
    }
  }
}
</script>
