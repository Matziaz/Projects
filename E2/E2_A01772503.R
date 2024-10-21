#Trabajar con las secuencias de los coronavirus de otras especies que son similares a SARS-CoV-2,
#para tratar de explicar el fenómeno de zoonosis del virus. 
#Incluye 20 especies reportadas. Puedes trabajar con variantes de SARS-CoV-2 de otros países.

# Librerías:
library(ape)
library(seqinr)
library(msaR)
library(Biostrings)

#PATH: "C:\Users\matia\OneDrive\Escritorio\E2\E2VIRUS\VIRUS"
# leer e imprimir las secuencias de los virus
setwd("C:/Users/matia/OneDrive/Escritorio/E2/E2VIRUS/VIRUS")
secuencias <- list.files(pattern="\\.fasta")
print(secuencias[])

# Calcula la longitud de las secuencias que incluyas
secuencias <- lapply(secuencias, function(x) {
  secuencia <- read.fasta(x,seqtype="DNA")
    return(nchar(secuencia[]))
})
print(secuencias)


# Gráfica de barras
barplot(unlist(secuencias), names.arg=secuencias, col=rainbow(20), las=2, cex.names=0.7, main="Longitud de las secuencias de los virus", ylab="Número de bases de ADN", xlab="Variantes del virus")

# INTERPRETACIÓN:
# La gráfica de barras muestra que las longitudes de las secuencias de los virus varían significativamente.
# Algunas secuencias tienen alrededor de 30,000 bases de ADN, mientras que otras alcanzan hasta 40,000 bases. 
# Esto sugiere una amplia diversidad en las secuencias virales, ya que no todas tienen la misma longitud. 
# Esta variabilidad en las longitudes puede deberse a diferencias en la estructura genómica de los virus, 
# así como a la diversidad de especies virales representadas en los datos.

# Convertir secuencias en un vector
secuencias <- unlist(secuencias, recursive = FALSE)
# Crear una matriz de distancias entre las secuencias
dist_matrix <- dist(as.matrix(secuencias))
# Realizar análisis jerárquico global (UPGMA)
arbol <- hclust(dist_matrix, method="average")

# INTERPRETACIÓN:
# El árbol filogenético del virus SARS-CoV-2 muestra cómo las secuencias están relacionadas en similitud genética.
# Ramas cercanas indican similitud, mientras que ramas distantes indican diferencias genéticas. 
# Esto ayuda a entender la diversidad genética, las relaciones evolutivas y las variantes del virus.


# Dibujar el Árbol Filogenético
plot(as.phylo(arbol), main="Dendrograma de las secuencias de virus")

# Dibujar el dendrograma de manera radial
plot(as.phylo(arbol), type="radial", main="Dendrograma de las secuencias de virus")


# Guardar el dendrograma y la gráfica de barras
png("dendrograma_virus.png")
plot(as.phylo(arbol), main="Arbol Filogenetico de las secuencias de virus")
dev.off()

png("barras_virus.png")
barplot(unlist(secuencias), names.arg=secuencias, col=rainbow(20), las=2, cex.names=0.7, main="Longitud de las secuencias de los virus", ylab="Número de bases de ADN", xlab="Variantes del virus")
dev.off()
