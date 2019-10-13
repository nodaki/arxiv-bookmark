<template>
  <div>
    <v-container fluid>
      <v-row justify="space-between">
        <v-col lg="10" md="10" sm="10">
          <v-autocomplete
            v-model="selectedCats"
            :items="allCategories"
            item-text="name"
            item-value="name"
            chips
            multiple
            hide-details
            solo
            clearable
            full-width
            label="Search by category"
            prepend-inner-icon="search"
            color="grey"
          >
            <template v-slot:selection="data">
              <v-chip
                v-bind="data.attrs"
                :input-value="data.selected"
                close
                @click="data.select"
                @click:close="remove(data.item)"
              >
                <span>{{ data.item.name }}</span>
              </v-chip>
            </template>
          </v-autocomplete>
        </v-col>
        <v-col lg="2" md="2" sm="2" class="mt-1">
          <v-btn icon color="blue" @click="search">
            <v-icon>search</v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { mapMutations, mapState } from 'vuex'
export default {
  name: 'SearchBox',
  data () {
    return {
      allCategories: [{ name: 'cs.CV' }, { name: 'stat.ML' }],
      selectedCats: []
    }
  },
  computed: {
    ...mapState({
      categories: state => state.categories
    })
  },
  methods: {
    ...mapMutations([
      'setCategories',
      'setInfiniteLoadingFlag'
    ]),
    remove (item) {
      const index = this.selectedCats.indexOf(item.name)
      if (index >= 0) { this.selectedCats.splice(index, 1) }
    },
    search () {
      this.setCategories(this.selectedCats)
      this.setInfiniteLoadingFlag(true)
    }
  }
}
</script>

<style scoped>

</style>
