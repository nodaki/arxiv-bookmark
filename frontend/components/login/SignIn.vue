<template>
  <div>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card>
          <v-card-text class="pb-0">
            <v-form>
              <p class="mb-0">
                Email
              </p>
              <v-text-field outlined dense name="email" type="text" />
              <p class="mb-0">
                Password
              </p>
              <v-text-field id="password" outlined dense name="password" type="password" />
            </v-form>
          </v-card-text>
          <v-card-actions class="pl-4 pr-4">
            <v-btn class="mb-2" color="success" block>
              Sign in
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: 'SignIn'
}
</script>

<style scoped>

</style>
