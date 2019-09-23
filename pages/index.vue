<template>
</template>

<script>

export default {
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
