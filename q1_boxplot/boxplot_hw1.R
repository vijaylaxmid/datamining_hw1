

# Loading the data
data<- c(197, 199, 234, 267, 269, 276, 281, 289, 299, 301, 339)

#??rainbow()--- Colors

c1 <- rainbow(10, start = 0.6)
c2 <- rainbow(10, alpha=0.2, start = 0.6)
c3 <- rainbow(10, v=0.7, start = 0.6)

#Opening the jpg file in the directory
#jpeg(filename = "boxplot.jpg")
boxplot(x= data, boxwex = 0.3, main= "Box Plot", horizontal= TRUE,outline = TRUE,
        col=c2,medcol=c3, whiskcol=c1, staplecol=c3, boxcol=c3, outcol=c3, pch=23, cex=2,
        notch= FALSE, varwidth = FALSE)

# data Labeling
text(x=fivenum(data), labels =fivenum(data),y=1.15, col = c1)

# Closing the file
dev.off()
